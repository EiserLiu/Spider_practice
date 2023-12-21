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

for i in range(0,61,20):
    print(f'https://movie.douban.com/review/best/?start={i}')