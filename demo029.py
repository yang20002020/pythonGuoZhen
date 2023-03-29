"""
for逻辑
for、in、range结合，遍历整数序列
for、in、list、dict结合，遍历容器内的元素
"""
# 用法一
for e in range(5):
    print(e)  # 0 1 2 3 4
print("----------------------")
# 用法二
for e in [3, 2, 1, 10]:
    print(e)
print("----------------------")
my_a = [3, 2, 1, 10]
for i in range(4):
    print(my_a[i])
print("----------------------")
for i in range(len(my_a)):
    print(my_a[i])

print("----------------------")
"""
案例
"""
a = [3, 1, 2, 5, 6]
b = []
a_len = len(a)
for i in range(a_len):
    if a[i] % 2 == 1:
        b.append(a[i] * 3 + 1)
        print(f'找到奇数{a[i]}')
    else:
        b.append(a[i] // 2)
        print(f'找到偶数{a[i]}')
print(b)
print("--------------------------------")
c = []
for e in a:
    if e % 2 == 1:
        c.append(e * 3 + 1)
        print(f'找到奇数{e}')
    else:
        c.append(e // 2)
        print(f'找到偶数{e}')
print(c)
