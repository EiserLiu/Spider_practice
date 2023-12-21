import requests

url = 'https://passport.17k.com/ck/user/login'

data = {
    'loginName': '1071519731',
    'password': '159753++',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 '
                  'Safari/537.36 Edg/118.0.2088.46'
}

res = requests.post(url, data=data, headers=headers)
print(res)
print(dict(res.cookies))
cookies = dict(res.cookies)
utl = "更新后的地址"
res = requests.get(url,headers=headers , cookies=cookies)
print(res)
print(res.text)