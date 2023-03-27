"""
量词
在python正则表达式中，量词用于指定匹配的次数，可以用在字符、字符集、分组等正则表达式元素上。常见的量词包括：
● *: 匹配前一个字符0次或者多次，等价于{0,};
● +:匹配前一个字符1次或者多次，等价于{1,};
● ？:匹配前一个字符0次或者1次，等价于{0,1};
● {m}:匹配前一个字符恰好m次；
● {m,n}:匹配前一个字符至少m次，至多n次。
"""
import re

result = re.findall(r"ab*c", "ac")
print(result)  # 输出['ac']
result = re.findall(r"ab+c", "ac")
print(result)  # 输出[]
result = re.findall(r"ab?", "a abb abbb")
print(result)  # 输出['a', 'ab', 'ab']

result = re.findall(r"ab+", "a abb abbb")
print(result)  # 输出['abb', 'abbb']
result = re.findall(r"ab*", "a abb abbb")
print(result)  # 输出['a', 'abb', 'abbb']
result = re.findall(r"ab{2}", "a abb abbb")
print(result)  # 输出['abb', 'abbb']
pattern = r".o{2}"
result = re.findall(pattern, "book great advertise tree wood")
print(result)  # ['boo', 'woo']
