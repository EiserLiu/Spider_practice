import urllib.request

url = 'http://www.baidu.com'
# 进行请求
response = urllib.request.urlopen(url)
print(response)
# 获取状态码
print(response.getcode())
# 获取url
print(response.geturl())
# 获取请求头
print(response.getheaders())
# 读取响应
print(response.read().decode("UTF-8"))
urllib.request.urlretrieve(url,filename='baidu.html')