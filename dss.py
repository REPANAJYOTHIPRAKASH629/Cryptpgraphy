#DSA-Digital Signature Standard
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.backends import default_backend
def generate_dsa_key():
  private_key=dsa.generate_private_key(key_size=1024,backend=default_backend)
  public_key=private_key.public_key()
  return private_key,public_key
def sign_message(private_key,message):
  signature=private_key.sign(message,hashes.SHA256())
  return signature
def verify_signature(public_key,signature,message):
  try:
    public_key.verify(signature,message,hashes.SHA256())
    return True
  except dsa.InvalidSignature:
    return False
private_key,public_key=generate_dsa_key()
message=b"Hello,DSA!"
signature=sign_message(private_key,message)
verification_result=verify_signature(public_key,signature,message)
print("Message:",message.decode('utf-8'))
print("Signature:",signature)
print("Verification Result:", verification_result)

OUTPUT:
Message: Hello,DSA!
Signature: b'0.\x02\x15\x00\xba\xdb\xff\xf5H\xf3\x88\xb1\xafQC\xa4)R\x01I\xac\xb0\xc2K\x02\x15\x00\xf4\xfe\xd3\xb8\x9bzv\xee\xda\xf3\xb9\x86\xf2\x87\xa1\xd0\x07\x00\xc0|'
Verification Result: True
