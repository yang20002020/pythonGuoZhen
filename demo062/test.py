"""
os.path.splitext
这个函数的意思是将文件的格式分开，比如输入为data/p1ch4/image-cats/add.png，
那么输出为(‘data/p1ch4/image-cats/add’, ‘.png’)，返回的是一个元组。
"""
import os

file_html_name = 'c_articles\\m0_59485658-Python画爱心——谁能拒绝用代码敲出来会跳动的爱心呢~-127748894.html'
pre_file_name = os.path.splitext(file_html_name)[0]
pre1=os.path.splitext(file_html_name)[1]
print(pre1)
print(type(pre_file_name))
print(pre_file_name)