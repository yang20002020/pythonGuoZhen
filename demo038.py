"""
常⻅的类型转化
"""
a = '123'
b = int(a)
print(b)
print(type(b))
a = 123
b = str(a)
print(b)

a = (1, 3, 2)  # 元组
print(type(a))  # <class 'tuple'>
b = list(a)  #
print(b)  # [1, 3, 2]

a = dict(a=1, b=2)
print(a)  # {'a': 1, 'b': 2}

a = [('a', 1), ('b', 2)]
b = dict(a)
print(b)  # {'a': 1, 'b': 2}
