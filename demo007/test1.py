s="人生苦短，我用python"
# 求字符串长度
a=len(s)
print(a)
# 获取前五个字符
s1=s[:5]
print(s1)
#获取字符串最后留个字符
s2=s[-6:]
print(s2)
#去掉多余的空格
s3="  "+s+"  "
print(s3)
s4=s3.strip()
print(s4)
#是否以某个串开头
b=s.startswith("人生苦短")
print(b)
#是否包括某个子串
k= '我' in s
print(k)

#串联多个字符串
s5="从零学python"
s6=';'.join([s,s5])
print(s6)
#分割字符串
s7=s6.split(';')
print(s7)
#替换字符串
s8=s6.replace("python","java")
print(s8)

