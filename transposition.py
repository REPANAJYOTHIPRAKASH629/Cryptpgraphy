import math

def columnar_transposition_encrypt(plain_text, key):
    n = len(key)
    plain_text = plain_text.replace(" ", "")  # Remove spaces
    num_rows = math.ceil(len(plain_text) / n)
    
    # Create the matrix for the plaintext
    matrix = [''] * n
    for i, char in enumerate(plain_text):
        matrix[i % n] += char
    
    # Sort the columns by the key and return the ciphertext
    sorted_key = sorted(list(key))
    cipher_text = ''
    for char in sorted_key:
        cipher_text += matrix[key.index(char)]
    return cipher_text

def columnar_transposition_decrypt(cipher_text, key):
    n = len(key)
    num_cols = len(cipher_text) // n
    sorted_key = sorted(list(key))
    
    # Reconstruct the column order
    columns = [''] * n
    index = 0
    for char in sorted_key:
        col_length = num_cols
        columns[key.index(char)] = cipher_text[index:index+col_length]
        index += col_length
    
    # Rebuild the plain text
    plain_text = ''
    for i in range(num_cols):
        for col in columns:
            if i < len(col):
                plain_text += col[i]
    
    return plain_text

# Example usage
key = input()
plain_text = input()
cipher_text = columnar_transposition_encrypt(plain_text, key)
print(f"Encrypted: {cipher_text}")

decrypted_text = columnar_transposition_decrypt(cipher_text, key)
print(f"Decrypted: {decrypted_text}")
