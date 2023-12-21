import time
import random
import requests
from lxml import etree

url = 'https://www.shicimingju.com/book/sanguoyanyi.html'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 "
                  "Safari/537.36 Edg/118.0.2088.46"
}
req = requests.get(url,headers=headers)
req.encoding='UTF-8'
# print(req.text)
tree = etree.HTML(req.text)

# 获取标题
title_list = tree.xpath('//div[@class="book-mulu"]/ul/li/a/text()')
# 获取超连接
href_list = tree.xpath('//div[@class="book-mulu"]/ul/li/a/@href')
for i in range(len(title_list)):
    # print(title_list[i])
    url = 'https://www.shicimingju.com'+href_list[i]
    # print(url)
    req = requests.get(url,headers=headers)
    req.encoding = 'UTF-8'
    # print(req.text)
    tree = etree.HTML(req.text)
    con = tree.xpath('//div[@class="card bookmark-list"]//text()')
    # print(title_list)
    print(con[0])
    time.sleep(random.randint(2,3))