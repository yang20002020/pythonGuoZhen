"""
正则分组
正则分组表达式中的分组指的是将正则表达式中的某个部分括号起来，以便于对这个部分进行操作或者提取。
在python的re模块中，可以使用圆括号（）来创建分组。
一个简单的例子是，可以使用()来匹配点在邮箱的前缀或者@后.com的电子邮件公司，并将这些数字作为一个分组。
例如：假设要匹配一个电子邮件地址，可以使用以下正则表达式：
"""
import re

pattern = r'(\w+)@(\w+)\.com'  # 正则表达式\.代表只匹配一个字符.
text = 'guozhennianhua@163.com'
match = re.search(pattern, text)
print(match)
print(match.group(1))  # 分组1 就是第一个（）中提取出来的内容  输出guozhennianhua
print(match.group(2))  # 分组2 就是将第一个（）中提取出来的内容   输出163
