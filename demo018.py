"""
冰雹序列
背景知识
数学中有⼀系列数字，有时被称为雹⽯序列。
考拉兹猜想（英语：Collatz conjecture），⼜称为奇偶归⼀猜想、冰雹猜想。
是指对于每⼀个正整数，如果它是奇数，则对它乘3再加1，如果它是偶数，则对它除以2，如此循
环，最终都能够得到1。
"""

number = int(input("请输⼊⼀个数字"))
a = [number]
while number > 1:
    if number % 2 == 1:
        number = number * 3 + 1
    else:
        number //= 2
    a.append(number)
print(a) // [9, 28, 14, 7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
