"""
映射计算
"""
a = len('苹果数是10')
print(a)
b = len([3, 1, [2, 0]])
print(b)

c = ord('郭')  # 返回  the Unicode code
print(c)  # 37101
d = ord('高')
print(d)  # 39640
print(ord('刘'))  # 21016

print(hex(ord('⾼')))  # 0x2fbc

a = sorted([1, 3, 2])
print(a)  # [1, 2, 3]
b = sorted(['郭', '高', '刘'])
print(b)  # ['刘', '郭', '高']

print("************************")

"""
map() 会根据提供的函数对指定序列做映射。
map(function, iterable, ...)
function -- 函数
iterable -- 一个或多个序列

"""


def f(x):
    return x + 1;


a = map(f, [3, 2, 10])
print(list(a))  # [4, 3, 11]

c = list(map(lambda x: x + 1, [3, 2, 10]))
print(c)  # [4, 3, 11]

a = [3, 2, 10]
b = [x + 1 for x in a]
print(b)  # [4, 3, 11]
a = list(reversed([3, 1, 2]))
print(a)  # [2, 1, 3]

print(sum([3, 1, 2]))  # 6
