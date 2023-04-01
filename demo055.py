import json

"""
JSON是⼀种轻量级的数据交换格式，常⽤于客服端与服务器间数据交换。
JSON是⼀种存储和交换数据的语法 
JSON仅仅是⽂本，它能够轻松地在服务器浏览器之间传输
"""
d = {'a': 1, 'b': 2}
d1 = json.dumps(d)
print(d1)  # 字符串格式 {"a": 1, "b": 2}
print(type(d1))  # <class 'str'>

json_str = '{"a":[1,3,2],"b":"it is book"}'
c = json.loads(json_str)
print(c)  # {'a': [1, 3, 2], 'b': 'it is book'}
print(type(c))  # <class 'dict'>
