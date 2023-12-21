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
    # 获取图片
    img = d.img
    # 获取标题
    title = d.h2.string
    # print(title)
    # 获取影评
    con = list(d.find('div', class_='short-content').stripped_strings)[0]

    # print(con)
    # 分析每个展开的url
    '''
    https://movie.douban.com/j/review/15499607/full
    https://movie.douban.com/j/review/15500693/full
    '''
    rid = d.find('div', id=re.compile("review_\d+_short"))['data-rid']
    # print(rid)
    req = requests.get(f'https://movie.douban.com/j/review/{rid}/full',
                       headers=headers)
    # 因为当前内容中包含HTML标签
    print(req.json()['html'])
    time.sleep(random.randint(1, 3))