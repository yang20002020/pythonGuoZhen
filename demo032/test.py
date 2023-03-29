"""
文件的读写
"""
# 读取文件
op_f = open("testFile.txt", 'r')
print(op_f.read())
op_f.close()
print("********************************")
with open("testFile.txt", 'r') as fr:
    print(fr.read())  # 不用再close操作
print("********************************")
# 文件写入
op_w = open("writeFile.txt", 'w')
s = 'hello world'
op_w.write(s)
op_w.close()
print("********************************")
with open("writeFile.txt", 'w') as op_w:
    s = 'hello world'
    op_w.write(s)
