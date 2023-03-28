"""
案例：输⼊区间内奇数和
"""

start = int(input("请输⼊左端点"))
end = int(input("请输⼊右端点"))
s = sum([e for e in range(start, end) if e % 2 == 1])
print(f'输⼊区间[{start},{end})的奇数和等于{s}')
