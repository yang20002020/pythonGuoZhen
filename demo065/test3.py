"""
RSA 加密机制
属于⾮对称加密，公钥⽤于对数据进⾏加密，私钥对数据进⾏解密，两者不可逆。公钥和私钥是
同时⽣成的，且⼀⼀对应。⽐如：A拥有公钥，B拥有公钥和私钥。A将数据通过公钥进⾏加密
后，发送密⽂给B，B可以通过私钥和公钥进⾏解密。
"""

from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as PKCS1_cipher

# 随机生成器
random_generator = Random.new().read
rsa = RSA.generate(2048, random_generator)

# 生成公钥
public_key = rsa.publickey().exportKey()
with open("public_a.rsa", "wb") as writer:
    writer.write(public_key)
print(public_key)

# 生成私钥
private_key = rsa.exportKey()
with open("private_a.rsa", "wb") as writer:
    writer.write(private_key)
print(private_key)

# 使用上面的一对公钥和私钥对数据data加密
data = input("请输入待加密的文本字符串")
with open('public_a.rsa', 'r') as reader:
    # 读取 公钥
    key = reader.read()
    #   公钥加密
    pub_key = RSA.importKey(str(key))
    cipher = PKCS1_cipher.new(pub_key)
    rsa_text = cipher.encrypt(data.encode("utf8"))  # 公钥加密

# 发送给客户端
with open("private_a.rsa", "r") as reader:
    key = reader.read()
    pri_key = RSA.importKey(key)
    cipher = PKCS1_cipher.new(pri_key)
    raw_data = cipher.decrypt(rsa_text, 0)
    print(f"使用私钥解密{rsa_text}\n后等于{raw_data.decode('utf8')}")
