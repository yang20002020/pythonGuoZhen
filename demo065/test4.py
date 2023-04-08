"""
AES 加密机制
属于对称加密，就是说，A⽤密码对数据进⾏AES加密后，B⽤同样的密码对密⽂进⾏AES解密。
"""
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

data = 'hello world'
# 随机生成秘钥
key = get_random_bytes(16)
print(f"key:{key}")
print(len(key))
mode = AES.MODE_OFB
#  生成 AES 钥匙 ；第三个参数是偏移量
aes_cryptor = AES.new(key, mode, b'0000000000000000')

# 字节数是16的倍数
length, count = 16, len(data)
add = 0
if count % length != 0:
    add = length - (count % length)
data += '\0' * add

#  加密文本
cipher_text = aes_cryptor.encrypt(data.encode('utf-8'))
print(f"加密文本cipher_text:{cipher_text}")

aes_cryptor = AES.new(key, mode, b'0000000000000000')  # aes_cryptor同上完全一致
raw_text = aes_cryptor.decrypt(cipher_text)
print(raw_text.decode('utf-8'))
