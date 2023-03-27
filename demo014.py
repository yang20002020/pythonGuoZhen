"""
列表中删除元素的三种方法

"""
a = [3, 7, 4, 2, 6]
print(a.pop())  # 6
print(a)  # [3, 7, 4, 2]

a = [3, 4, 5, 6]
print(a.remove(4))  # None
# remove 删除对应的元素  只移除列表中的第一个对应的元素值
print(a)  # [3, 5, 6]
a = [3, 7, 1, 2, 4, 5, 4]
a.remove(4)
print(a)  # [3, 7, 1, 2, 5, 4]

# del在指定索引位置删除对应的元素
a = [3, 7, 4, 2, 6]
del a[3]
print(a)  # [3, 7, 4, 6]
if 10 in a:
    a.remove(10)
else:
    print("10不在列表a中")
