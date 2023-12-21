import requests
from bs4 import BeautifulSoup

url = 'https://www.quheqihuo.com/news/202310133104866.html'
# 请求网址
response = requests.get(url)
# 设置编码
response.encoding = 'UTF-8'
# 获取HTML内容
html = response.text
# 实例化bs4对象
soup = BeautifulSoup(html, 'lxml')
# 解析 匹配
# 因为当前table的border为0,所以查找的时候限定为0
table = soup.find('table', attrs={'border': '0'})
# print(table)
# 查找所有tr
tr = table.find_all('tr')
# print(tr)
for t in tr:
    # print(t)
    td = t.find_all('td')
    # print(td[0].text)
    for i in td:
        print(i)

# if not td:
#     break
#     print('品种:', td[0].text, '报价', td[1].text, '材质', td[2].text, '规格', td[3].text, '钢厂', td[4].text)
