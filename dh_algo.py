# prompt: b) Implementation of Diffie-Hellman Algorithm in python i need simple code i need to collect user input

import random

def diffie_hellman():
  """Implements the Diffie-Hellman key exchange."""

  # Shared prime number and base (agreed upon beforehand)
  p = int(input("Enter a prime number (p): "))
  g = int(input("Enter a base (g): "))

  # Alice's private key
  a = random.randint(1, p - 1)
  print("Alice's private key (a):", a)

  # Alice's public key
  A = (g ** a) % p
  print("Alice's public key (A):", A)

  # Bob's private key
  b = random.randint(1, p - 1)
  print("Bob's private key (b):", b)

  # Bob's public key
  B = (g ** b) % p
  print("Bob's public key (B):", B)

  # Alice calculates the shared secret
  shared_secret_a = (B ** a) % p
  print("Alice's shared secret:", shared_secret_a)

  # Bob calculates the shared secret
  shared_secret_b = (A ** b) % p
  print("Bob's shared secret:", shared_secret_b)

  if shared_secret_a == shared_secret_b:
    print("Shared secret successfully established!")
  else:
    print("Error: Shared secrets do not match.")

if __name__ == "__main__":
  diffie_hellman()
