"""
字符集
在python  re模块中，字符集用于指定匹配的字符范围。
普通字符：可以在字符集中使用普通的ASCII字符。例如，字符集[a-z]表示匹配所有小写字母。
范围：字符集中可以使用“-”来指定字符范围。例如字符集[a-z]表示匹配所有小写字母。
排除字符：字符集中可以使用“^”符号来排除一些字符。例如，字符集[^a-z]表示匹配所有不是小写字母的字符。
"""
import re

pattern = r'[a-d]'
result = re.findall(pattern, "book great advertise cat")
print(result)

pattern = r'[^a-d]'
result = re.findall(pattern, "book great advertise cat")
print(result)