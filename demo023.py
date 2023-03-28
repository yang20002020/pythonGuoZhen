"""
 更新字典
修改原有键
添加键值对
"""

d = {'a': 10, 'b': 8, 'c': 18}
# 修改原有键
d['c'] = 90
print(d)
# 添加键值对
d.update({'d': 19, 'e': 20})
print(d)  # {'a': 10, 'b': 8, 'c': 90, 'd': 19, 'e': 20}

"""
删除字典键值对
pop某个键值对
del某个键值对
"""
d = {'a': 10, 'b': 8, 'c': 18}
print(d.pop("c"))  # 18
print(d)  # {'a': 10, 'b': 8}
d = {'a': 10, 'b': 8, 'c': 18}
del d['c']
print(d)  # {'a': 10, 'b': 8}

# 批量删除
d = {'a': 10, 'b': 8, 'c': 90, 'd': 19, 'e': 20}
del_keys = ['a', 'c', 'e']
for del_key in del_keys:
    del d[del_key]
print(d)  # {'b': 8, 'd': 19}
