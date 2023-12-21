import asyncio



async def run():
    print("run函数开始")
    await asyncio.sleep(2)
    print("run函数结束")

if __name__ == '__main__':
    con = run()
    # asyncio.run(con)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(con)
