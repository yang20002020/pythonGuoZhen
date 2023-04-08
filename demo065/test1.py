"""
生成公钥 ，生成对应的公钥txt文件

RSA 加密机制 
属于⾮对称加密，公钥⽤于对数据进⾏加密，私钥对数据进⾏解密，两者不可逆。公钥和私钥是 
同时⽣成的，且⼀⼀对应。⽐如：A拥有公钥，B拥有公钥和私钥。A将数据通过公钥进⾏加密 
后，发送密⽂给B，B可以通过私钥和公钥进⾏解密。 
"""

from Crypto import Random
from Crypto.PublicKey import RSA

# 随机生成器
random_generator = Random.new().read
rsa = RSA.generate(2048, random_generator)

# 生成公钥
public_key = rsa.publickey().exportKey()
with open("public_a.rsa", "wb") as writer:
    writer.write(public_key)
print(public_key)
