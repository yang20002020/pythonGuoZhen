"""
抽样红⻩蓝球
"""
import random

balls = ['红球1', '红球2', '红球3',
         '⻩球4', '⻩球5', '⻩球6',
         '蓝球7', '蓝球8', '蓝球9']
a = random.choices(balls, k=9)  # 有放回抽样9次
print(a)
a = random.sample(balls, k=9)  # 没有放回抽取
print(a)
