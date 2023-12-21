import asyncio
import aiohttp



async def main():
    async with aiohttp.ClientSession() as session:
        params = {'name': 'lzp', 'age': 18}
        async with session.get('http://httpbin.org/headers', params=params) as response:
            print(response.url)
            return await response.text()


asyncio.run(main())
