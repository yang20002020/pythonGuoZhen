"""
lambda 函数
"""


# def max(*args, key=None)
def max_len(*l):
    return max(*l, key=lambda v: len(v))


a = max_len([3, 2, 1], [1], [3, 5, 7, 1, 4])
print(a)  # [3, 5, 7, 1, 4]
