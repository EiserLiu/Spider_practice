import requests
from lxml import etree
from bs4 import BeautifulSoup

url = 'https://app.mi.com/catTopList/0?page=1'
# 请求网址
response = requests.get(url)
# 设置编码
response.encoding = 'UTF-8'
# 获取HTML内容
# print(response.text)
tree = etree.HTML(response.text)
# 匹配应用名称
# app_name = tree.xpath('//ul[@class="applist"]/li/h5/a/text()')
# print(appname)
# 匹配应用连接
# link = tree.xpath('//ul[@class="applist"]/li/h5/a/@href')
# print(link)
# 匹配名称和连接
val = tree.xpath('//ul[@class="applist"]/li/h5/a/text() | //ul[@class="applist"]/li/h5/a/@href')
# print(val)
for i in range(0, len(val), 2):
    print('href:', 'https://app.mi.com' + val[i], '名称:', val[i + 1])
