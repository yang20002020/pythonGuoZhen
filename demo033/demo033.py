import json

d = {"姓名": "小明", "身高": 1.85, }
d["性别"] = "男"
print(d)
s = json.dumps(d)
print(type(s))  # <class 'str'>
# {"\u59d3\u540d": "\u5c0f\u660e", "\u8eab\u9ad8": 1.85, "\u6027\u522b": "\u7537"}
print(s)
{"姓名": "小明", "身高": 1.85, "性别": "男"}
s = json.dumps(d, ensure_ascii=False)
print(s)  # {"姓名": "小明", "身高": 1.85, "性别": "男"}
print(type(s))  # <class 'str'>

#  'a' open for writing, appending to the end of the file if it exists
with open("20230329.txt", 'a') as w_f:
    w_f.write(s)
