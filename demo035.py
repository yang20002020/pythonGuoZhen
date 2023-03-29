"""
实现⻩⾦分割序列函数
⻩⾦分割序列函数⼜被称为斐波那契数列，在⾃然界中此序列较为常⻅。
它的第⼀项是1，第⼆项是1，第三项是2，并且后⾯各项满⾜规律：
"""


def fibo(n):
    i = 0
    fibo_list = []
    while i < n:
        if i == 0 or i == 1:
            fibo_list.append(1)
        if i >= 2:
            thd = fibo_list[-1] + fibo_list[-2]
            fibo_list.append(thd)
        i += 1
    return fibo_list


print(fibo(3))
print(fibo(5))
