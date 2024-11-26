#HMAC
import hmac
import hashlib
def generate(key,message):
  hash_function=hashlib.sha256
  key=bytes(key,'utf-8')
  hmac_res=hmac.new(key,bytes(message,'utf-8'),digestmod=hash_function)
  hmac_hex=hmac_res.hexdigest()
  return hmac_hex
secret_key='my_secret_key'
data_to_hash="Hello, HMAC!"
res=generate(secret_key,data_to_hash)
print("Input Message:",data_to_hash)
print("Secret Key:",secret_key)
print("HMAC Output:",res)

OUTPUT:
Input Message: Hello, HMAC!
Secret Key: my_secret_key
HMAC Output: 2135134b3d2d6ac11a8eb3f6340dac59282a4edbb21ba861772ab2cb3ca56942
