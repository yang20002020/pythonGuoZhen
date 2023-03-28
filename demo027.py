"""
 set内增删元素
"""
b = {1, 2, 3}
b.add(10)
print(b)  # {10, 1, 2, 3}
b.add(1)
print(b)  # {10, 1, 2, 3}

print(b.pop())  # 10
print(b)  # {1, 2, 3}
print(b.pop())  # 1
print(b)  # {2, 3}
b.remove(3)
print(b)  # {2}

print("***********************")
"""
set间操作
"""

c = {3, 1, 2}
d = {9, 8, 1, 3, 10}
print(c | d)  # {1, 2, 3, 8, 9, 10}

print(c & d)  # {1, 3}
print(c - d)  # {2}
print(d - c)  # {8, 9, 10}
print(c.issubset(d))  # False
print({3, 1}.issubset(d))  # True
