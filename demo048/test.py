"""
遍历文件夹的两种方式
listdir
walk
"""
import os

for file in os.listdir("jackguo/"):
    print(file)
print("************************")
"""
递归查找每一个层级文件
"""
for path, folders, files in os.walk("jackguo/"):
    print(path, folders, files)
