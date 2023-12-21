import requests

url = 'http://www.baidu.com'
response = requests.get(url)
# print(response)
# 打印响应内容
response.encoding = 'UTF-8'
# print(response.text)
# print(response.content.decode('UTF-8'))

# 获取请求的URL
# print(response.url)

# 获取状态码
# print(response.status_code)

# 获取响应对应的请求头
# print(response.request.headers)

# 获取响应的cookie
# print(response.cookies)

# print(response.ok)
