import requests
from lxml import etree

proxy = {
    'http': 'http://182.34.101.162:9999'
}

url = 'https://www.luffycity.com/actual-course?page=1'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 '
                  'Safari/537.36 Edg/118.0.2088.46'

}

data = {
    'username': "15130784895",
    'password': "Tyc20030124"
}

session = requests.Session()

response = session.post(url, headers=headers, data=data, proxies=proxy)

response.encoding = 'UTF-8'

tree = etree.HTML(response.text)

print(tree.xpath('//div[@class=]'))