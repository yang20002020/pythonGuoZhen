""""
编码实现输⼊圆半径计算周⻓和⾯积
"""
import math

r = input("请输⼊圆的半径: ")
f_r = float(r)
c = 2*math.pi*f_r
print(f"圆的周⻓等于{c:.2f}")# 保留两位小数
s = math.pi*f_r**2
print(f"圆的⾯积等于{s:.2f}")