import time
from multiprocessing import Process


def get_data(url):
    # 请求爬取数据
    # requests.get
    # print(new_url)
    print(url)
    time.sleep(1)


if __name__ == '__main__':
    url = 'http://www.baidu.com?page='
    for i in range(10):
        nuw_url = url + str(i)
        Process(target=get_data, args=(nuw_url,)).start()
