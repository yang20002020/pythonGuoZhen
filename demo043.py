"""
案例：清洗各地苹果产量字典
apples = {'天⽔': '1000', '静宁': '800',
 '⽩⽔': '1200', '烟台': '2000', '延安': '1100'}

 apples2 = {'天⽔': 1000, '静宁': 800,
 '⽩⽔':1200, '烟台':2000, '延安':1100}
两种⽅法：
1. 普通⽅法
2. map⽅法
"""
# 普通⽅法
apples = {'天⽔': '1000', '静宁': '800',
          '⽩⽔': '1200', '烟台': '2000', '延安': '1100'}
apples2 = dict()
for k, v in apples.items():
    apples2[k] = int(v)
    print((k, int(v)))

print(apples2)

# map⽅法
apples = {'天⽔': '1000', '静宁': '800',
          '⽩⽔': '1200', '烟台': '2000', '延安': '1100'}


def f(k):
    return (k, int(apples[k]))


apples2 = dict(map(f, apples))
print(apples2)
