import re
"""
元字符：元字符是正则表达式中用来匹配字符的特殊字符。
例如：
 "."表示匹配任意字符；
“^”表示匹配字符串的开头；
“$”表示匹配字符串的结尾等；
python中 import re封装的正则相关的函数
"""
text = """每经AI快讯：北京时间3月27日11:30，上证指数早盘下跌34.37点，跌幅为1.05%，报收3231.28点，成交额3036.67亿元；深证成指下跌71.06点，跌幅为0.61%，报收11563.16点，成交额4638.23亿元；创业板指上涨10.72点，涨幅为0.45%，报收2381.1点，成交额2101.82亿元；沪深300下跌38.28点，跌幅为0.95%，报收3988.77点，成交额2158.7亿元。
涨幅前五的行业分别是电子化学品3.13%、风电设备2.77%、光伏设备1.63%、医疗服务1.57%、医疗器械1.05%。
跌幅前五的行业分别是保险-2.36%、房地产服务-2.31%、游戏-2.28%、水泥建材-2.0%、房地产开发-2.0%。"""

print(text)
# 使用正则表达式提取任意单个字符
pattern = r"."
result = re.findall(pattern, text)
print(result)  # 输出的是一个数组
print("************")
# 使用正则表达式提取文本开头首字符
pattern1 = r"^."
result1 = re.findall(pattern1, text)
print(result1)
# 使用正则表达式提取文本最后的字符
pattern2 = r".$"
result2 = re.findall(pattern2, text)
print(result2)
# 查找文本中的某个字符 比如 点
pattern3 = r"点"
result3 = re.findall(pattern3, text)
print(result3)
# 查找文本中 开头的字符是不是以某个字符开头
pattern4 = r"^点"
result4 = re.findall(pattern4, text)
print(result4)
