import random
import time
from lxml import etree
import requests
from lxml import etree
from bs4 import BeautifulSoup
import json

'''
https://movie.douban.com/top250?start=0&filter=
https://movie.douban.com/top250?start=25&filter=
'''

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 '
                  'Safari/537.36 Edg/117.0.2045.60',
    'Referer': 'https: // movie.douban.com / explore',
    'Cookie': 'll="118093"; bid=0f8caXYvfMs; ap_v=0,6.0; '
              '__utma=30149280.647042964.1697341520.1697341520.1697341520.1; __utmc=30149280; '
              '__utmz=30149280.1697341520.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt_t1=1; '
              '__utmb=30149280.18.8.1697343539005; RT=s=1697343654094&r=https%3A%2F%2Fmovie.douban.com%2Fexplore'
}

for i in range(1, 6):
    # 如果代码有错,添加异常处理
    try:
        start = (i - 1) * 25
        url = f'https://movie.douban.com/top250?start={start}&filter='
        # print(url)
        print(f'第{i}页数据')
        response = requests.get(url, headers=headers)
        # print(response.text)
        # 匹配到每个电影里的li里的div
        tree = etree.HTML(response.text)
        div = tree.xpath('//*[@id="content"]/div/div[1]/ol/li/div')
        # print(div)
        for d in div:
            # 获取当前电影序号
            num = d.xpath('./div/em/text()')[0]
            # 获取电影标题
            title = d.xpath('.//span[@class="title"][1]/text()')[0]
            print(num, title)
    except Exception as e:
        print(e, url)
    time.sleep(random.randint(1, 3))
