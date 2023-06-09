"""
beautiful soup4
"""
from bs4 import BeautifulSoup
import lxml

my_page = '''<html>
 <title>程序员zhenguo</title>
    <body>
          <h1>我的⽹站</h1>
          <div>我的⽂章</div>
          <div id="photos">
               <img src="pic1.png" />
               <span id="pic1"> 从零学Python </span>
               <img src="pic2.png" />
               <span id="pic2" >⼤纲</span>
               <p>
                 <a href="http://www.zglg.work">更多详情</a>
                </p>
               <a href="http://www.zglg.work/python-packages/">Python
               <a href="http://www.zglg.work/python-intro/">Python⼩⽩
               <a href="http://www.zglg.work/python-level/">Python进阶
          </div>
          <div id="explain">
               <p class="md-nav__item">本站总访问量159323次</p>
          </div>
          <div class="foot">Copyright © 2019 - 2021 程序员zhenguo</div>
    </body>
 </html>'''

soup = BeautifulSoup(my_page, 'lxml')

# 定位所有a标签
# 方法一
a_results = soup.find_all('a')
print(a_results)
print("-----------------------------------")
# 方法二
a_results2 = soup.select('a')
print(a_results2)
print("-----------------------------------")
# 定位 所有带id的div标签
id_divs = soup.select('div[id]')
print(id_divs)
print("-----------------------------------")
# 定位id等于photos的div标签
# 方法一
photos_div = soup.find_all('div', attrs={'id': 'photos'})
print(photos_div)
print("-----------------------------------")
# 方法二
photos_div2 = soup.select("div[id='photos']")
print(photos_div2)
print("-----------------------------------")

# 查找 所有 href 属性取值
for item in soup.select('[href]'):
    print(item['href'])
