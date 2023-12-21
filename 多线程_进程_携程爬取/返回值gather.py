import asyncio


# 异步任务
async def run(url):
    print('协程', url, '开始')
    return url


# 回调函数
def call_back(f):
    print('返回值', f.result())


async def main():
    url_list = ['baidu.con', 'taobao.con', 'aiqiyi.con']
    tasks = []
    for url in url_list:
        con = run(url)
        task = loop.create_task(con)
        # task.add_done_callback(call_back)
        tasks.append(task)
    done = await asyncio.gather(*tasks)
    for f in done:
        print('获取返回值', f)
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
