"""
元组
元组的长度是固定不变的，不能增加删除
"""
a = ('2021-04-01', '开盘', 3010)
print(a)
print(a[0])
b = ()
print(b)
print(type(b))
c = tuple(['2021-04-01', '开盘', 3010])
print(c)  # ('2021-04-01', '开盘', 3010)
print(c.count(3010))  # 1
print(c.index(3010))  # 2
