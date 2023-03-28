# 思考题：如何更安全的访问某个字典？
d = {'a': 10, 'b': 8, 'c': 18}
print(d)
# 如果不存在 返回None
print(d.get('f', None))  # None
# 如果不存在 返回0
print(d.get("f", 0))  # 0
