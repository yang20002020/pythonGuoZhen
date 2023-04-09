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
print('---------------')
pattern = r"h.*"  # (.*) 贪婪匹配,代表尽可能多的匹配字符因此它将h和l之间所有的字符都匹配了出来
result = re.findall(pattern, "hello school html hlight hl")
print(result)  # ['hello school html hlight hl']
pattern = r"h.*?l"
result = re.findall(pattern, "hello school html hlight hl")
print(result)  # ['hel', 'hool', 'html', 'hl', 'ht hl']
pattern = r"h(.*?)l"  # (.*?) 懒惰匹配尽可能匹配少的字符但是要匹配出所有的字符
result = re.findall(pattern, "hello school html hlight hl")
print(result)  # ['e', 'oo', 'tm', '', 't h']
