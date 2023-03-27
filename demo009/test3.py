import re

"""
        特殊序列
         正则表达式中，特殊序列是一些具有特殊意义的转移序列，它们以反斜杠\为前缀。
        下面列举几个常用的正则表达式特殊序列：
        \d:匹配任意一个数字字符，相当于[0-9];
        \D:匹配任意一个非数字字符，相当于[^0-9]
        \w:匹配任意一个字母、数字或者下划线字符，相当[a-zA-Z0-9_];
        \W:匹配任意一个非字母、数字或者下划线字符，相当于[^a-zA-Z0-9_];
        \s:匹配任意一个空白字符，包括空格、制表符、和换行符。
        \S:匹配任意一个非空白字符，不包括空格、制表符和换行符。
        \b:匹配单词边界，包括单词前面或者后面的空格、标点符号或者字符串边界；
        \B：匹配非单词边界，不包括单词前面或者后面的空格、标点符号或者字符串边界；
        \A:匹配字符串开头；
        \Z：匹配字符串结尾；
"""
pattern = r"\d"
text = "abc123def"
result = re.findall(pattern, text)
print(result)  # ['1', '2', '3']

pattern = r"\D"
text = "abc123def"
result = re.findall(pattern, text)
print(result)  # ['a', 'b', 'c', 'd', 'e', 'f']

pattern = r"\W"
text = "abc_123_def"
result = re.findall(pattern, text)
print(result)  # []

pattern = r"\bfoo\b"  # 匹配一个单词 "foo"
text = "foo bar foo."
result = re.findall(pattern, text)
print(result)  # ['foo', 'foo']

pattern = r"\Afoo"  # 匹配以"foo"开头的字符串
text = "foo bar foo."
result = re.findall(pattern, text)
print(result)  # ['foo']
