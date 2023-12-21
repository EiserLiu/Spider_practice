import requests

url = 'http://www.baidu.com/img/bd_logo1.png'
response = requests.get(url)
# print(response)

# response.encoding = 'UTF-8'

# print(response.ok)
with open('baidu.jpg', 'wb') as f:
    f.write(response.content)
# print(response.content)
