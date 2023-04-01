# 发送post请求
# 传递表单
import requests

payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.post('http://httpbin.org/post', data=payload)
print(r.text)
"""
显示了对应的表单:
  "form": {
    "key1": "value1", 
    "key2": "value2"
  }, 
  打印结果如下:
{
  "args": {}, 
  "data": "", 
  "files": {}, 
  "form": {
    "key1": "value1", 
    "key2": "value2"
  }, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Content-Length": "23", 
    "Content-Type": "application/x-www-form-urlencoded", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.25.1", 
    "X-Amzn-Trace-Id": "Root=1-64283873-79ccf2a725d19fb612e68e92"
  }, 
  "json": null, 
  "origin": "183.197.243.50", 
  "url": "http://httpbin.org/post"
}
"""
