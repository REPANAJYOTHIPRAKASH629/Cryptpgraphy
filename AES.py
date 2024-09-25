!pip install pycryptodome

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

# AES encryption function
def aes_encrypt(plain_text, key):
    cipher = AES.new(key, AES.MODE_CBC)  # Using CBC mode
    ct_bytes = cipher.encrypt(pad(plain_text.encode('utf-8'), AES.block_size))
    return cipher.iv, ct_bytes

# AES decryption function
def aes_decrypt(cipher_text, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plain_text = unpad(cipher.decrypt(cipher_text), AES.block_size)
    return plain_text.decode('utf-8')

key = get_random_bytes(16) 
plain_text = input()

iv, cipher_text = aes_encrypt(plain_text, key)
print(f"Encrypted text: {cipher_text}")
decrypted_text = aes_decrypt(cipher_text, key, iv)
print(f"Decrypted text: {decrypted_text}")
