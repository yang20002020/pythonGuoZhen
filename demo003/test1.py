w = input("请输⼊天⽓情况(可选项：晴天、阴天):")
fri_n = input("请输⼊打球伙伴数：")
fri_n = int(fri_n)
if w == "晴天":
    if fri_n >= 3:
        print("我们去打球吧")
    else:
        print(f"⼈⼿不够")
else:
    print(f"天⽓{w}不打球")
