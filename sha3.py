#SHA-3
import sys
import hashlib
if sys.version_info<(3,6):
  import sha3
s=hashlib.sha3_224()
print(s.name)
print(s.digest_size)
s.update(b"Geeks")
print(s.hexdigest())

OUTPUT:
sha3_224
28
a32d875e701e4b6b0c582d39562fa989e1f4b6dfc17e45ad22fee234
