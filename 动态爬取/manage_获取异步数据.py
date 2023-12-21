import requests
from lxml import etree
from bs4 import BeautifulSoup
import json

url = ('https://m.douban.com/rexxar/api/v2/movie/recommend?refresh=0&start=20&count=20&selected_categories=%7B%22%E7'
       '%B1%BB%E5%9E%8B%22:%22%22%7D&uncollect=false&tags=&playable=true&sort=S')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 '
                  'Safari/537.36 Edg/117.0.2045.60',
    'Referer': 'https: // movie.douban.com / explore',
    'Cookie': 'll="118093"; bid=0f8caXYvfMs; ap_v=0,6.0; '
              '__utma=30149280.647042964.1697341520.1697341520.1697341520.1; __utmc=30149280; '
              '__utmz=30149280.1697341520.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt_t1=1; '
              '__utmb=30149280.18.8.1697343539005; RT=s=1697343654094&r=https%3A%2F%2Fmovie.douban.com%2Fexplore'
}

response = requests.get(url, headers=headers)
# print(response)
print(response.json())
subjects = response.json()['recommend_categories']
for i in subjects:
    print(i)
