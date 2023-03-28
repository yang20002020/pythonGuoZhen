"""
if else
"""
x = input("输⼊⼀个整数: ")
if 0 < int(x) < 255:  # 注意写法没有&
    print("这是⼩正整数")
elif int(x) >= 255:
    print("这是⼤正整数")
else:
    print("这是负数")
