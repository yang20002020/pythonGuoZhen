"""
os模块
"""
import os

a = os.name
print(a)  # nt  操作系统名称
b = os.curdir
print(b)  # . 当前目录

c = os.sep
print(c)  # \  文件分隔符

d = 'python3.7' + os.sep + 'jackGuo'
print(d)

e = os.linesep
print(e)  # 换行符

if not os.path.exists("jackgui"):
    print("文件不存在")
