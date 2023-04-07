"""
step1: 爬取博主的所有博文的article_ids
step2: 根据article_id，爬取这篇文章的html，拿到我们想要的部分，并且
step3: 保存为html格式，再保存一个可读性更好的pdf格式

例如： https://blog.csdn.net/m0_59485658
username=m0_59485658
需要下载安装包，地址： https://wkhtmltopdf.org/downloads.html
windows环境下需要配置对应的exe文件 环境变量
"""
import os
import random
import time
import requests
from lxml import etree
import pdfkit

author_name = input("请输入博主ID: ")
MAX_PAGE_NUM = 200  # 最多200页
i = 1  # i代表第几篇博文

sess = requests.Session()
agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
sess.headers['User-Agent'] = agent

# 根据 用户名 文章id和文章名称 爬取文章内容
def crawler_blog_by(author_name, article_id, title):
    #  article_request_url  是一篇博文的地址对应的字符串
    #  例如 ：https://blog.csdn.net/m0_59485658/article/details/129720168
    article_request_url = f"https://blog.csdn.net/{author_name}/article/details/{article_id}"
    response = sess.get(article_request_url)  # response: <Response [200]>
    #   print(type(response))  # <class 'requests.models.Response'> 的对象类型就是 Response
    # response.text 对应  上述网页的源代码  即 对应的网址右键 =》检查   查看源代码
    selector = etree.HTML(response.text)
    head_msg = selector.xpath(r"//head")[0]  # selector.xpath()返回的是列表
    #   上述网页的源代码  即 对应的网址右键查看源代码 <head>部分
    head_str = etree.tostring(head_msg, encoding='utf8', method='html').decode()
    body_msg = selector.xpath(r"//div[@id='content_views']")[0]

    #   上述网页的源代码  即 对应的网址右键查看源代码 <div id="content_views" 部分
    body_str = etree.tostring(body_msg, encoding='utf8', method='html').decode()

    if not os.path.exists("c_articles"):
        os.mkdir('c_articles')

    title = title.replace("/", "-").replace(":", "").replace(": ", "")
    # save_file_name=  'c_articles\\m0_59485658-Python画爱心——谁能拒绝用代码敲出来会跳动的爱心呢~-127748894.html'
    save_file_name = os.path.join('c_articles', f'{author_name}-{title}-{article_id}.html')
    with open(save_file_name, 'w', encoding='utf8') as writer:
        writer.write(f"""<head> <meta charset="utf-8" </head>
                      {body_str}""")

        html_to_pdf(save_file_name)
        global i
        print(f'【INFO】: {author_name}第{i}篇博文{title}-{article_id}.html保存文件成功')
        i += 1


def html_to_pdf(file_html_name):
    pre_file_name = os.path.splitext(file_html_name)[0]
    wkhtmltopdf_options = {'enable-local-file-access': None}
    pdfkit.from_file(file_html_name, pre_file_name + '.pdf', options=wkhtmltopdf_options)


# 循环爬取分页html

for page_no in range(MAX_PAGE_NUM):
    try:
        ## 前端 payload
        #  例如 https://blog.csdn.net/m0_59485658  右键=》检查=》滚动鼠标滑轮=》载荷
        data = {"page": page_no,
                "size": 20,
                "businessType": "blog",
                "orderby": "",
                "noMore": False,
                "year": "",
                "month": "",
                "username": author_name}
        # get参数 具体查询的步骤，按demo061.png图片介绍所示
        #  pages_dict 每一页字典
        pages_dict = sess.get('https://blog.csdn.net/community/home-api/v1/get-business-list',
                              params=data).json()
        # 参考demo061_1.png， 获取pages_dict['data']['list']
        for article in pages_dict['data']['list']:
            article_id = article['articleId']
            title = article['title']
            crawler_blog_by(author_name, article_id, title)

        time.sleep(random.uniform(0.4, 1.0))
    except Exception as e:
        print(e)  # log日志文件系统
