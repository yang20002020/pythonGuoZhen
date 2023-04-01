"""
案例:
生成一个由六位数组成的验证码
"""
import random

yanzhengma = [random.randint(0, 9) for _ in range(6)]
print(yanzhengma)

yzm = map(str, yanzhengma)
print(yzm)
print(''.join(yzm))
