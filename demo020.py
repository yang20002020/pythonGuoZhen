"""
创建字典两种方法
"""
d = {}
print(d)  # {}
d['a'] = 10
print(d)  # {'a': 10}

d['b'] = 8
print(d)  # {'a': 10, 'b': 8}
print("______________")
d = dict()
print(d)  # {}
d = dict(a=10, b=9)
print(d)  # {'a': 10, 'b': 9}

d = dict([('a', 10), ('b', 8)])
print(d) # {'a': 10, 'b': 8}
