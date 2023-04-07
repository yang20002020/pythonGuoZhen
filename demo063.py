"""
引入hashlib包 实现md5加密
"""
import hashlib

obj = hashlib.md5()
data = 'hello world'
obj.update(data.encode('utf-8'))
str = obj.hexdigest()
print(str)   # 5eb63bbbe01eeed093cb22bb8f5acdc3
