import urllib.request
import urllib.parse
import json
from multiprocessing import Process


def kfc(num):
    # 拿到地址
    url = "http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/117.0.0.0'
                      'Safari/537.36 Edg/117.0.2045.60'
    }
    # 获取到当前浏览器请求锁携带的表单数据
    print(f"第{num}页")
    form_Data = {
        'cname': '',
        'pid': '',
        'keyword': '北京',
        'pageIndex': num,
        'pageSize': 10
    }
    # 对表单数据进行转码
    form_Data = urllib.parse.urlencode(form_Data).encode('UTF-8')
    # 发送post请求
    request = urllib.request.Request(url, data=form_Data, headers=headers)
    response = urllib.request.urlopen(request)
    # 返回JSON数据 转换成字典
    data = json.loads(response.read().decode('UTF-8'))
    # print(data["Table1"])
    for l in data["Table1"]:
        print(l)


if __name__ == '__main__':
    for i in range(1, 10):
        Process(target=kfc, args=(i,)).start()
