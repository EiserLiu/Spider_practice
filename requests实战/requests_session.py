import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 "
                  "Safari/537.36 Edg/118.0.2088.46"
}
# 先访问首页 获取到cookie
session = requests.Session()  # 创建一个session对象
main_url = 'https://xueqiu.com/'
session.get(url=main_url, headers=headers)

# 访问异步加载的地址 携带者cookie过去
url = 'https://xueqiu.com/statuses/hot/listV2.json?since_id=-1&max_id=551612&size=15'
proxies = {'http': 'IP:端口'}
res = session.get(url, headers=headers)
print(res)
print(res.json())
