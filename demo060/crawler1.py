# 爬取tuke88的配乐mp3文件

import os
import random
import time
import requests
import lxml.etree

print(os.path)  # <module 'ntpath' from 'D:\\anaconda3\\lib\\ntpath.py'>
page_n = int(input("请输入你想爬取的网页数量"))

for i in range(page_n):
    url = f'http://www.tuke88.com/peiyue/zonghe_0_{i}.html'
    response = requests.get(url)
    print(f"response.text:{response.text}") # html文件
    # 爬虫第三步: lxml框架提取html网页我们想要的内容

    html_parser = lxml.etree.HTMLParser()  #  # 为了 防止html语法错误
    html = lxml.etree.fromstring(response.text, parser=html_parser)
    titles = html.xpath("//div[@class='lmt']//div[@class='audio-list']//a[@class='title']/text()")
    mp3_urls = html.xpath("//div[@class='lmt']//div[@class='audio-list']//source/@src")
    if not os.path.exists("pymp3"):
        os.mkdir('pymp3')
    for title, mp3_url in zip(titles, mp3_urls):
        mp3_stream = requests.get(mp3_url, stream=True) # 流式下载 一部分一部分下载
        with open(os.path.join('pymp3', title + '.mp3'), 'wb+') as writer:
            writer.write(mp3_stream.raw.read())
            print(f"【INFO】{title}.mp3下载成功")
            time.sleep(random.uniform(0.1, 0.4))
