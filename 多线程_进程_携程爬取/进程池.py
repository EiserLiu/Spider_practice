import time
from multiprocessing import Pool,cpu_count


def get_data(url):
    # 请求爬取数据
    # requests.get
    # print(new_url)
    print(url)
    time.sleep(10)


if __name__ == '__main__':
    # 进程别太多,容易把服务器搞崩
    '''
    url = 'http://www.baidu.com?page='
    pool = Pool()  # 传参 开启几个进程  #默认开启核心数个CPU
    for i in range(10):
        url = 'http://www.baidu.com?page=' + str(i)
        pool.apply_async(get_data, args=(url,))
    pool.close()
    pool.join()
    print("主进程结束")
    '''
    print(cpu_count())