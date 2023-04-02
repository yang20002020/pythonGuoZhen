# 我们爬取网页的目的，无非是先定位到DOM树的节点，然后取其文本或属性值
"""
lxml定位、取text、取属性值

"""

from lxml import etree

my_page = '''<html>
                <title>程序员zhenguo</title>
                <body>
                    <h1>我的网站</h1>
                    <div>我的文章</div>
                    <div id="photos">
                        <img src="pic1.png" />
                        <span id="pic1"> 从零学Python </span>
                        <img src="pic2.png" />
                        <span id="pic2" >大纲</span>
                        <p>
                            <a href="http://www.zglg.work">更多详情</a>
                        </p>
                        <a href="http://www.zglg.work/python-packages/">Python包</a>
                        <a href="http://www.zglg.work/python-intro/">Python小白</a>
                        <a href="http://www.zglg.work/python-level/">Python进阶</a>
                    </div>
                    <div id="explain">
                        <p class="md-nav__item">本站总访问量159323次</p>
                    </div>
                    <div class="foot">Copyright © 2019 - 2021 程序员zhenguo</div>
                </body>
        </html>'''

html = etree.fromstring(my_page)

# 一、定位
# 共四个 div
# //div 代表所有的div
divs1 = html.xpath('//div')
# //div[@id] 返回所有带有id的div
divs2 = html.xpath('//div[@id]')
#  返回class="foot的所有div
divs3 = html.xpath('//div[@class="foot"]')
#  //div[@*] 返回所有带有属性的div
divs4 = html.xpath('//div[@*]')

divs5 = html.xpath('//div[1]')

divs6 = html.xpath('//div[last()]')

divs7 = html.xpath('//div[position()<3]')

divs8 = html.xpath('//div|//h1')
#  //div[not(@*)]  返回所有没有带有属性的div
divs9 = html.xpath('//div[not(@*)]')

# 二、取文本 text() 区别 html.xpath('string()')
text1 = html.xpath('//div/text()')
text2 = html.xpath('//div[@id]/text()')
text3 = html.xpath('//div[@class="foot"]/text()')
text4 = html.xpath('//div[@*]/text()')
text5 = html.xpath('//div[1]/text()')
text6 = html.xpath('//div[last()-1]/text()')
text7 = html.xpath('//div[position()<3]/text()')
text8 = html.xpath('//div/text()|//h1/text()')

# 三、取属性 @
value1 = html.xpath('//a/@href')
value2 = html.xpath('//img/@src')
value3 = html.xpath('//div[@id]/span/@id')

# 四、定位（进阶）
# 1.文档(DOM)元素(Element)的find，findall方法
divs = html.xpath('//div[position()<3]')
for div in divs:
    ass = div.findall('a')  # 这里只能找到:div->a, 找不到:div->p->a
    for a in ass:
        if a is not None:
            # print(dir(a))
            print(a.text, a.attrib.get('href'))  # 文档(DOM)元素(Element)的属性：text, attrib

# 2.与1等价
a_href = html.xpath('//div[position()=2]/a/@href')
print(a_href)

# 3.注意与1、2的区别
a_href = html.xpath('//div[position()=2]//a/@href')
print(a_href)
