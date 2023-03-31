import derectors  # 运行该文件 filter.py  会打印 :  模块的名字derectors

print(derectors.module_name)  # derectors

derectors.print_me()  # 这个模块的名字叫derectors

tc = derectors.TestClass()
print(tc)  # name=zhengguo,age=32,height=171
tc.height = 173
print(tc)  # name=zhengguo,age=32,height=173
