"""
列表生成式
"""
a = [3, 7, 4, 2, 6]
b = [e * 2 for e in a]
print(b)  # [6, 14, 8, 4, 12]
c = [e * 2 for e in a if e % 2 == 0]
print(c)  # [8, 4, 12]
"""
案例：
输⼊列表a，返回⼀个包括其中所有偶数的列表
两种写法
⼀种不使⽤列表⽣成式
另⼀种使⽤列表⽣成式

"""
a = input("请输⼊⼀个列表")  # 例如 [3,1,2]
a = eval(a)  # 字符串转换为列表
print("不使⽤列表⽣成式")
b = list()  # []
for e in a:
    if e % 2 == 0:
        b.append(e)
print(b)
print("使⽤列表⽣成式")
c = [e for e in a if e % 2 == 0]
print(c)
