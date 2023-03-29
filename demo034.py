"""
自定义函数
"""


def sumRange(start, end):
    sumRange = 0
    for i in range(start, end + 1):
        if i % 2 == 0:
            sumRange += i
    print(f'{start}-{end}区间偶数和等于{sumRange}')
    return sumRange


a = sumRange(10, 20)
print(a)
