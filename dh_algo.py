#Diffie-Hellman
import random
p=23
q=5
def compute_public_key(private_key):
  return (q**private_key)%p
private_key_a=random.randint(1,p-1)
private_key_b=random.randint(1,p-1)
public_key_a=compute_public_key(private_key_a)
public_key_b=compute_public_key(private_key_b)
shared_secret_a=(public_key_b**private_key_a)%p
shared_secret_b=(public_key_a**private_key_b)%p
print(shared_secret_a)
print(shared_secret_b)
