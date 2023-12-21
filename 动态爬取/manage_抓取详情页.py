import random
import re
import time
from lxml import etree
import requests
from lxml import etree
from bs4 import BeautifulSoup
import json

'''
抓取单页影评
抓取单页 展开的影评
抓取单页当前影评的详情页
抓取多页 展开的影评及其详情页
'''

url = 'https://movie.douban.com/review/best/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 '
                  'Safari/537.36 Edg/117.0.2045.60,',

}
response = requests.get(url, headers=headers)
# print(response.text)
soup = BeautifulSoup(response.text, 'lxml')
# 找到每条影评数据
div = soup.find_all('div', class_='main review-item')
# print(div)
for d in div:
    # 匹配详情页的连接
    href = d.a['href']
    # print(href)
    response = requests.get(href,headers=headers)
    data = response.text
    #进行详情页内容的处理
    detail_soup = BeautifulSoup(data,'lxml')
    info = detail_soup.find('div', id='link-report-intra').text
    print(href)
    print(info)

    time.sleep(random.randint(2,5))
    # print(data)