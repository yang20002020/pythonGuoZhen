"""
random 模块
"""
import random

a = random.randint(1, 10)
print(a)

random_ints = [random.randint(1, 10) for _ in range(100)]
print(random_ints)

occur_dict = dict()
for integer in random_ints:
    if integer not in occur_dict:
        occur_dict[integer] = 1
    else:
        occur_dict[integer] += 1
print(occur_dict)

print("*****************")
print(random.random())  # 0.7224441941643941
print(random.uniform(1, 10))  # 5.4044578596676045

# 有放回的抽取
a = random.choice(random_ints)
print(a)

# 无放回的抽取  ????
print(random_ints)
print(random.sample(random_ints, 3))
print(random_ints)
