"""
案例：计算⼩明考试的总分、平均分和⽅差
分别提示输⼊⼩明的语⽂、数学、英语、物理、化学、地理的考试分数
⾃动打印出他的考试总分、平均分、⽅差

"""
yuwen = int(input("请输⼊⼩明的语⽂分数"))
shuxue = int(input("请输⼊⼩明的数学分数"))
yingyu = int(input("请输⼊⼩明的英语分数"))
wuli = int(input("请输⼊⼩明的物理分数"))
huaxue = int(input("请输⼊⼩明的化学分数"))
dili = int(input("请输⼊⼩明的地理分数"))
sum_grade = yuwen + shuxue + yingyu + wuli + huaxue + dili
avg_grade = sum_grade / 6
squ = (yuwen - avg_grade) ** 2 + (shuxue - avg_grade) ** 2 + \
(yingyu - avg_grade) ** 2 + (wuli - avg_grade) ** 2 + \
(huaxue - avg_grade) ** 2 + (dili - avg_grade) ** 2
squ = squ / 6
print(f"考试总分: {sum_grade}")
print(f"考试平均分: {avg_grade:.2f}")
print(f"考试⽅差: {squ:.2f}")