import random
def gcd(a, b):
  if b == 0:
    return a
  return gcd(b, a % b)

def generate_keypair(p, q):
  n = p * q
  phi = (p - 1) * (q - 1)
  e = random.randrange(1, phi)
  g = gcd(e, phi)
  while g != 1:
    e = random.randrange(1, phi)
    g = gcd(e, phi)
  d = pow(e, -1, phi)
  return ((e, n), (d, n))

def encrypt(pk, plaintext):
  key, n = pk
  cipher = [(ord(char) ** key) % n for char in plaintext]
  return cipher

def decrypt(pk, ciphertext):
  key, n = pk
  plain = [chr((char ** key) % n) for char in ciphertext]
  return ''.join(plain)

if __name__ == '__main__':
  p = 61
  q = 53
  print("Generating your public/private keypairs now . . .")
  public, private = generate_keypair(p, q)
  print("Your public key is ", public, " and your private key is ", private)
  message = 'Hello World!'
  encrypted_msg = encrypt(public, message)
  print("Your encrypted message is: ")
  print(''.join(map(lambda x: str(x), encrypted_msg)))

  print("Decrypting message with private key ", private, " . . .")
  decrypted_msg = decrypt(private, encrypted_msg)
  print("Your message is:")
decrypted_msg
