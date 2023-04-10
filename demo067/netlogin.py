"""
模拟登陆
"""

from DecryptLogin import login

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
    'Accept': '*/*'
}


class NetLogin:
    def __init__(self, username, password):
        self.user_name = username
        self.password = password

    def log_in(self):
        lg = login.Login()
        _, session = lg.music163(self.user_name, self.password)
        return session


if __name__ == "__main__":
    nl = NetLogin("158*****", "***dou2017")
    sess = nl.log_in()
    print(f"sess:{sess}")
