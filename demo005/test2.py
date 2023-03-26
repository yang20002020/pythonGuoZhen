subjects = ["语⽂", "数学", "英语", "物理", "化学", "地理"]
grades = []
for sub in subjects:
    grades.append(int(input(f"请输⼊⼩明的{sub}分数")))

sum_grade = sum(grades)
avg_grade = sum_grade / len(subjects)
squ = sum([(gra - avg_grade) ** 2 for gra in grades]) / len(subjects)
print(f"考试总分: {sum_grade}")
print(f"考试平均分: {avg_grade:.2f}")
print(f"考试⽅差: {squ:.2f}")
