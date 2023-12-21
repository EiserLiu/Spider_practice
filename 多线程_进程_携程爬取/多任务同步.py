import asyncio
import time


async def run(url):
    print(f'开启请求{url}的数据')
    await asyncio.sleep(2)
    print(f'结束请求{url}的数据')
    data = url + "抓取的数据"
    return data

def call_back(f):
    print(f.result())


if __name__ == '__main__':
    t1 = time.time()
    loop = asyncio.get_event_loop()
    url_list = ['baidu.com', 'taobao.com', 'aiqiyi.com']
    tasks = [] # 包含多个task任务的对象
    for i in url_list:
        con = run(i)
        # 开启消息循环
        task = asyncio.ensure_future(con)
        # 添加回调函数
        task.add_done_callback(call_back)
        tasks.append(task)
    loop.run_until_complete(asyncio.wait(tasks))
    print(time.time() - t1)