"""
提取股票文字中数值
例如：截止收盘，上证指数上涨0.78%，报3446.73点，深证成指涨0.91%,报13642.95点，
创业板指涨1.06%,报2672.12点。指数午后震荡走高，碳中和概念强者恒强，板块内上演涨停潮，环保、物业
特高压板块午后涨幅扩大，数字货币板块尾盘冲高，高铁、煤炭、有色板块全天较为低迷，题材股午后整体回暖，两市
上涨个股逾3000家。赚钱效益较好。
"""
import re

pattern = '-?\d+\.\d+%'  # -? 表示 -出现0次或者1次
my_str = """例如：截止收盘，上证指数上涨0.78%，报3446.73点，深证成指涨0.91%,报13642.95点，
创业板指涨1.06%, 报2672.12点。指数午后震荡走高，碳中和概念强者恒强，板块内上演涨停潮，环保、物业
特高压板块午后涨幅扩大，数字货币板块尾盘冲高，高铁、煤炭、有色板块全天较为低迷，题材股午后整体回暖，两市
上涨个股逾3000家。赚钱效益较好。"""
print(my_str)
result = re.findall(pattern, my_str)
print(result)  # ['0.78%', '0.91%', '1.06%']
print("******************")
my_str2 = re.sub(pattern, '', my_str)
print(my_str2)
print("******************")
pattern2 = '-?\d+\.\d+'
result2 = re.findall(pattern2, my_str2)
result.extend(result2)
print(result)
print("******************")
my_str3 = re.sub(pattern2, '', my_str)
print(my_str3)
print("******************")
pattern3='-?[1-9]\d*' # 0开头的数字不符合标准
result3= re.findall(pattern3,my_str3)
result.extend(result3)
print(result)
