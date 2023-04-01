import requests

# get请求
r = requests.get('http://httpbin.org/get')
# 传递参数
params = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('http://httpbin.org/get', params=params)
"""
r.text 返回编码解析的结果
r.content返回⼆进制结果
r.json()返回字典，可能抛出异常
r.status_code
r.raw返回原始socket response，需要加参数stream=True
"""
"""
1** 信息，服务器收到请求，需要请求者继续执⾏操作
2** 成功，操作被成功接收并处理
3** 重定向，需要进⼀步的操作以完成请求
4** 客户端错误，请求包含语法错误或⽆法完成请求
5** 服务器错误，服务器在处理请求的过程中发⽣了错误
"""
print(r.status_code)  # 200
print(f"r.text:{r.text}")
"""
r.text:{
  "args": {
    "key1": "value1", 
    "key2": "value2"
  }, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.25.1", 
    "X-Amzn-Trace-Id": "Root=1-6427f581-073cab2b0396741a0665f23c"
  }, 
  "origin": "183.197.243.50", 
  "url": "http://httpbin.org/get?key1=value1&key2=value2"
}
"""
print("------------------------------------")
print(f"r.content:{r.content}")

print("------------------------------------")
print(f"r.json:{r.json()}")
print("------------------------------------")
# raw 返回原始socket response
r = requests.get('http://httpbin.org/get', stream=True)
print(f"r.raw:{r.raw}")
with open("httpbin.txt", 'w') as wr:
    wr.write(r.raw.read().decode('utf8'))
# 传递headers
headers = {'user-agent': 'my-app/0.0.1'}
r = requests.get('http://httpbin.org/get', headers=headers)
# 传递cookies
url = 'http://httpbin.org/cookies'
r = requests.get(url, cookies=dict(cookies_equ='cache info'))
r.text

print(r.text)
