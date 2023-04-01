"""
time 模块
"""
import time

now = time.localtime()
print(now)
a = time.strftime("%Y-%m-%d %H:%M:%S", now)
print(a)  # 2023-04-01 09:52:28
a = time.time()
b = time.ctime(a)
print(b) # Sat Apr  1 09:54:46 2023
