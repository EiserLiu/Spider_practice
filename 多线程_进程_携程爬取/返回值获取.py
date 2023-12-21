import asyncio
import json

import aiohttp

async def fetch(session,url):
    async with session.post(url,data='传递数据') as response:
        # return await response.text()
        return await response.json()

async def main():
    async with aiohttp.ClientSession() as session:
        source = await fetch(session, 'http://httpbin.org/post')
        # print(json.loads(source))
        print(source)

asyncio.run(main())
