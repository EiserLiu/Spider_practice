import asyncio
import aiohttp

async def fetch(session,url):
    async with session.get(url) as response:
        return await response.text()


async def main():
    async with aiohttp.ClientSession() as session:
        source = await fetch(session, 'http://httpbin.org/headers')
        print(source)


asyncio.run(main())
