"""
Асинхронный веб-скрапинг
"""
import asyncio

import aiofiles
import aiohttp
import bs4

digits = []
sem = asyncio.Semaphore(20)


async def read_url(session, url):
    async with sem:
        async with session.get(url) as response:
            if response.status == 200:
                soup = bs4.BeautifulSoup(await response.text(), 'html.parser')
                p_tags = soup.find('p', id='number').text
                digits.append(int(p_tags))

async def main():
    tasks = []
    session = aiohttp.ClientSession()
    async with aiofiles.open("problem_pages.txt", mode="r") as f:
        async for line in f:
            tasks.append(asyncio.create_task(read_url(session, f"https://asyncio.ru/zadachi/2/html/{line}.html")))


    await asyncio.gather(*tasks)
    await session.close()
    print(sum(digits))


if __name__ == '__main__':
    asyncio.run(main())