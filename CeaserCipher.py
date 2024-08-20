def encrypt(text, key):
    encrypted = ""
    for char in text:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            encrypted += chr((ord(char) - shift + key) % 26 + shift)
        else:
            encrypted += char
    return encrypted

def decrypt(text, key):
    return encrypt(text, -key)

text = input("Enter any String: ")
key = int(input("Enter the Key: "))

encrypted_text = encrypt(text, key)
print("\nEncrypted String is:", encrypted_text)

decrypted_text = decrypt(encrypted_text, key)
print("\nDecrypted String is:", decrypted_text)
