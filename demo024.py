"""
⽔果分类
题⽬描述
已知常⻅⽔果和它的分类，求得分类和⽔果的字典。
输⼊列表如下所示：
fruits = [('桃' , '核果类'),('杏', '核果类'), ('李', '核果类'), ('樱
桃', '核果类'), ('苹果', '仁果类'),('梨','仁果类'),('⼭楂', '仁果类')]
"""

fruits = [('桃', '核果类'), ('杏', '核果类'), ('李', '核果类'),
          ('樱桃', '核果类'), ('苹果', '仁果类'), ('梨', '仁果类'),
          ('⼭楂', '仁果类')]

print(fruits)
fruit_dict = {}
for e in fruits:
    fruit, cat = e[0], e[1]
    print(f"e[0]{e[0]}")
    print(f"e[1]{e[1]}")
    if cat not in fruit_dict:
        fruit_dict[cat] = [fruit]  # 值 是列表
    else:
        fruit_dict[cat].append(fruit)  # {'核果类': ['桃', '杏', '李', '樱桃'], '仁果类': ['苹果', '梨', '⼭楂']}
print(fruit_dict)
