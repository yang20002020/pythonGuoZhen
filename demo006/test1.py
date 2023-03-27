"""
输⼊⼀个⼈名，返回其unicode编码
"""
name = input("请输⼊⼀个名字：")
uc = ''  # 空字符串
for w in name:
    print(ord(w))
    print(hex(ord(w)))
    uc += r'\u' + hex(ord(w))[2:] #去掉0x
    # r  字符原生表示法
    # ord（）函数  返回the Unicode code
    # hex 返回 16进制 例如  0xc0ffee
print(f'unicode编码等于{uc}')
