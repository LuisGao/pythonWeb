from lxml import etree
import requests


response = requests.get('https://www.geekdigging.com/')
html_str = response.content.decode('UTF-8')
html = etree.HTML(html_str) # 构件一个lxml.etree.Element对象，理解为一个XML的Doc

# Print Document
result = etree.tostring(html, encoding = 'UTF-8').decode('UTF-8')
print(result)

# Node Select:
# root 就是Document自己了
# root下一级节点
rChild = html.xpath('/*')

# 匹配特定节点
result_2 = html.xpath('//meta')
print(result_2)

# 获取特定节点下所有内容
result_3 = html.xpath('//main/article')

# 属性过滤 [@para='value']
result_7 = html.xpath('//section/div[@class="container"]')
print(result_7)

# 快捷获取：浏览器开发者工具邮件得到xpath
# 如：//*[@id="post-485"]
# 其他条件语法：
# 1.add语法：//img[@class="img-ajax" and @alt="小白学 Python 爬虫（18）：Requests 进阶操作"]
# 2.多重条件语法： '//div[contains(@class, "post-head")]
# 详见专门的xpath教程




a = 1 + 1


