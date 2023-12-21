import urllib.request

url = 'https://www.baidu.com/s?tn=44004473_8_oem_dg&ie=utf-8&wd='
# key_word = '迪丽热巴'
key_word = input('输入搜索内容:')
# url转码
url += urllib.request.quote(key_word)
# print(url)
# print(urllib.request.unquote(url))
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 '
                  'Safari/537.36 Edg/117.0.2045.60'
}
#构造请求对象
request = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(request)
print(response.read().decode('utf-8'))
# with open('baidu.html', 'wb') as f:
#     f.write(response.read())
