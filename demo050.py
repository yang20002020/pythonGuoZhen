"""
统计程序运行时间
"""
import time

t1 = time.perf_counter()
print(t1)
for i in range(10):
    time.sleep(1)
    print(f'run {i}')
t2 = time.perf_counter()
print(t2)
print(f'运⾏时⻓{t2 - t1}s')
