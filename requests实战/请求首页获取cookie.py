import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 "
                  "Safari/537.36 Edg/118.0.2088.46"}

main_url = 'https://xueqiu.com/'
response_main = requests.get(main_url, headers=headers)
# print(response_main)
# 获取服务器端响应的cookie
cookies = response_main.cookies
# print(response_main.cookies)
# print(dict(cookies))

url = 'https://xueqiu.com/statuses/hot/listV2.json?since_id=-1&max_id=551612&size=15'

response = requests.get(url,headers=headers,cookies=cookies)
print(response)