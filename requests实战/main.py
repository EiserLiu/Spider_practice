import os.path
import random
import time

import requests
from lxml import etree
from urllib import request as req

url = "http://pic.netbian.com/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 "
                  "Safari/537.36 Edg/118.0.2088.46"}

response = requests.get(url, headers=headers)
response.encoding = 'GBK'
# print(response.text)
tree = etree.HTML(response.text)
li = tree.xpath('//ul[@class="clearfix"]/li')
for i in li:
    # 获取图片url
    hrfe = i.xpath('./a/span/img/@src')
    # 拼凑完整url
    image_url = 'http://pic.netbian.com/' + hrfe[0]
    image_name = i.xpath('./a/b/text()')[0]
    # print(image_url)
    path = './img'
    if not os.path.exists(path):
        os.mkdir(path)
    req.urlretrieve(image_url, os.path.join(path,image_name+".jpg"))
    print(image_name)
    time.sleep(random.randint(2,3))