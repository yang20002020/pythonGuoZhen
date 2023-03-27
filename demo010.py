"""
创建列表的三种方法
"""
# 方法1
a = []
print(a)
print("----------------")
a = [3, 1, 2]
print(a)  # [3, 1, 2]
print("----------------")
# 方法2
a = list((3, 1, 2))
print(a)  # [3, 1, 2]
print("----------------")
# 方法3
range(10)  # [0,10)
for i in range(10):
    print(i)
a = list(range(10))
print(a)
