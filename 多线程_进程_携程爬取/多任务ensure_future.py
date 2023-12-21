import asyncio


# 异步任务
async def run(url):
    print('协程', url, '开始')
    return url


# 回调函数
def call_back(f):
    print('返回值', f.result())


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    tasks = []
    url_list = ['baidu.con', 'taobao.con', 'aiqiyi.con']
    for url in url_list:
        con = run(url)
        # 创建任务
        task = asyncio.ensure_future(con)
        task.add_done_callback(call_back)
        tasks.append(task)
    loop.run_until_complete(asyncio.wait(tasks))
    print('over')
