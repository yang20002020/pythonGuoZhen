print(locals())
import derectors

print(locals())
#  相对上面的打印  多出：  'derectors': <module 'derectors' from 'D:\\PycharmProjects\\pythonGuoZhen\\demo044\\chat_app\\derectors.py'>


print(derectors.module_name)  # derectors

derectors.print_me()  # 这个模块的名字叫derectors

tc = derectors.TestClass()
print(tc)  # name=zhengguo,age=32,height=171
tc.height = 173
print(tc)  # name=zhengguo,age=32,height=173
