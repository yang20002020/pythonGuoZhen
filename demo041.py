"""
内置函数
id 、 range、 enumerate、 zip
"""
# help

a = help(id)  # Return the identity of an object.
print(a)  # None

a = [3, 1, 2]
print(id(a))  # 1714026094528
b = [3, 4, 10]
print(id(b))  # 2681769532544

print(list(range(1, 11)))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# enumerate
a = [3, 1, 2]
for i, e in enumerate(a):
    print(f"列表a的索引等于{i}")
    print(f"列表a的对应元素值等于{e}")
#  zip
a = [3, 1, 2]
b = [10, 6, 8]
for i, j in zip(a, b):
    print(f'i={i},j={j}')
print("******************")
a = [3, 1, 2]
b = [10, 6, 8, 1, 10, 4, 5]
for i, j in zip(a, b):
    print(f'i={i},j={j}')
