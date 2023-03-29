"""
判断某个数是否为素数
素数定义：只能被1和本身整除

"""
import math
a = int(input("请输⼊⼀个整数"))
if a <= 3:
    print(f'{a}是素数')

is_prime = True
for i in range(2, int(math.sqrt(a)) + 1):
    if a % i == 0:
        print(f'{a}不是素数')
        is_prime = False
        break
if is_prime:
    print(f"{a}是素数")
