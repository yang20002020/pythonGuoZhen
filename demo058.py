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
a_results = soup.find_all('a')
print(a_results)
print("-----------------------------------")
a_results2 = soup.select('a')
print(a_results2)
