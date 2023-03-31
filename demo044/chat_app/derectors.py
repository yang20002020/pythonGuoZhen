module_name = __name__
print(f"模块的名字{module_name}")  # 运行文件 derectors.py  打印的结果是： 模块的名字__main__


def print_me():
    print(f"这个模块的名字叫{module_name}")


class TestClass:
    def __init__(self):
        self.name = "zhengguo"
        self.age = 32
        self.height = 171

    def __repr__(self):
        return f"name={self.name},age={self.age},height={self.height}"
