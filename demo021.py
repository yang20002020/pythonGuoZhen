"""
遍历字典
"""
d = dict([('a', 10), ('b', 8)])
d['c'] = 18
print(d)  # {'a': 10, 'b': 8, 'c': 18}
# 获取键
print(d.keys())  # dict_keys(['a', 'b', 'c'])

print(list(d.keys()))  # ['a', 'b', 'c']
# 获取值
print(d.values())  # dict_values([10, 8, 18])
print(list(d.values()))  # [10, 8, 18]
# 获取键值对
print(d.items())  # dict_items([('a', 10), ('b', 8), ('c', 18)])
print(list(d.items()))  # [('a', 10), ('b', 8), ('c', 18)]

# 遍历 键
for k in d:
    print(k, d[k])

for k, v in d.items():
    print(k, v)
