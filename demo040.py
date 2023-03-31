"""
思考题：使⽤两种以上⽅法计算列表平⽅
已知列表a=[3,1,2,5]，返回⼀个每个元素都平⽅后的新列表b
"""
a = [3, 1, 2, 5]
b = [i ** 2 for i in a]
print(b)  # [9, 1, 4, 25]

a = [3, 1, 2, 5]


def f(i):
    return i ** 2


b = list(map(f, a))
print(b)  # [9, 1, 4, 25]