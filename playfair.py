def generate_playfair_key_matrix(key):
    matrix = []
    key = key.upper().replace("J", "I")
    key += ''.join([chr(i) for i in range(65, 91) if chr(i) != 'J'])  # A-Z without 'J'
    
    seen = set()
    for char in key:
        if char not in seen and char.isalpha():
            matrix.append(char)
            seen.add(char)
    return [matrix[i:i + 5] for i in range(0, 25, 5)]

def find_position(char, matrix):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col
    return None

def playfair_encrypt(plain_text, key):
    matrix = generate_playfair_key_matrix(key)
    plain_text = plain_text.upper().replace("J", "I")
    plain_text = ''.join([c for c in plain_text if c.isalpha()])
    
    if len(plain_text) % 2 != 0:
        plain_text += 'X'
    
    cipher_text = ''
    for i in range(0, len(plain_text), 2):
        a, b = plain_text[i], plain_text[i+1]
        row1, col1 = find_position(a, matrix)
        row2, col2 = find_position(b, matrix)
        
        if row1 == row2:
            cipher_text += matrix[row1][(col1+1) % 5] + matrix[row2][(col2+1) % 5]
        elif col1 == col2:
            cipher_text += matrix[(row1+1) % 5][col1] + matrix[(row2+1) % 5][col2]
        else:
            cipher_text += matrix[row1][col2] + matrix[row2][col1]
    
    return cipher_text

def playfair_decrypt(cipher_text, key):
    matrix = generate_playfair_key_matrix(key)
    plain_text = ''
    
    for i in range(0, len(cipher_text), 2):
        a, b = cipher_text[i], cipher_text[i+1]
        row1, col1 = find_position(a, matrix)
        row2, col2 = find_position(b, matrix)
        
        if row1 == row2:
            plain_text += matrix[row1][(col1-1) % 5] + matrix[row2][(col2-1) % 5]
        elif col1 == col2:
            plain_text += matrix[(row1-1) % 5][col1] + matrix[(row2-1) % 5][col2]
        else:
            plain_text += matrix[row1][col2] + matrix[row2][col1]
    
    return plain_text

key = input()
plain_text = input()
cipher_text = playfair_encrypt(plain_text, key)
print(f"Encrypted: {cipher_text}")

decrypted_text = playfair_decrypt(cipher_text, key)
print(f"Decrypted: {decrypted_text}")
