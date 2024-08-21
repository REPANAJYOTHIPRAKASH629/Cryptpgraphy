def prepare_text(text):
    text = text.upper().replace("J", "I").replace(" ", "")
    if len(text) % 2 != 0:
        text += "X"
    return text

def create_matrix(key):
    key = key.upper().replace("J", "I")
    matrix = []
    for char in key + "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in matrix:
            matrix.append(char)
    return [matrix[i:i+5] for i in range(0, 25, 5)]

def find_position(matrix, char):
    for i, row in enumerate(matrix):
        if char in row:
            return i, row.index(char)

def encrypt(plain_text, key):
    matrix = create_matrix(key)
    plain_text = prepare_text(plain_text)
    cipher_text = ""

    for i in range(0, len(plain_text), 2):
        row1, col1 = find_position(matrix, plain_text[i])
        row2, col2 = find_position(matrix, plain_text[i+1])

        if row1 == row2:
            cipher_text += matrix[row1][(col1+1)%5] + matrix[row2][(col2+1)%5]
        elif col1 == col2:
            cipher_text += matrix[(row1+1)%5][col1] + matrix[(row2+1)%5][col2]
        else:
            cipher_text += matrix[row1][col2] + matrix[row2][col1]

    return cipher_text

# Input
key = input("Enter the key: ")
plain_text = input("Enter the plaintext: ")

# Output
cipher_text = encrypt(plain_text, key)
print("Encrypted text:", cipher_text)
