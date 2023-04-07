"""
使用MD5技术实现用户名和密码的验证登录
"""

import hashlib


def get_md5(data):
    obj = hashlib.md5()
    obj.update(data.encode('utf-8'))
    return obj.hexdigest()


def register():
    user_name = input("请输⼊注册的⽤户名")
    user_pwd = input("请输⼊注册⽤户名密码")
    with open('user_jiami.txt', 'w') as writer:
        writer.write(get_md5(user_name))
        writer.write('\n')
        writer.write(get_md5(user_pwd))
        print('注册成功')


register()


def check_ok(user_name, user_pwd):
    name = get_md5(user_name)
    pwd = get_md5(user_pwd)
    with open('user_jiami.txt', 'r') as reader:
        lines = reader.readlines()  # 1行1行读
    print(f"name={name}, pwd={pwd},lines[0]={lines[0]}, lines[1]={lines[1]}")
    return str(lines[0]).strip() == str(name) and str(lines[1]).strip() == pwd


def login():
    """已注册⽤户的登⼊"""
    user_name = input("请输⼊⽤户名")
    user_pwd = input("请输⼊密码")
    if check_ok(user_name, user_pwd):
        print('登⼊成功')
        #  """登⼊成功进⼊⾸⻚"""
        return "登⼊成功"
    else:
        print('登⼊失败')
        login()


login()