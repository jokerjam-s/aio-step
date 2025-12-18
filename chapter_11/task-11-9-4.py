"""
Рекурсивный асинхронный веб-скрапинг (глубина 2)
"""
base_url = "https://asyncio.ru/zadachi/3/index.html"

import asyncio

import aiohttp
import bs4

digits = []
sem = asyncio.Semaphore(25)


async def read_url(session, url):
    links = []
    async with sem:
        async with session.get(url) as response:
            if response.status == 200:
                soup = bs4.BeautifulSoup(await response.text(), 'html.parser')
                # Находим тег для извлечения числа
                number_tag = soup.find('p', {'id': 'number'})
                # Находим все ссылки на странице
                links = soup.find_all('a', {'class': 'link'})
                if number_tag:
                    digits.append(int(number_tag.text))

    for link in links:
        url_next = url.rsplit('/', 1)
        await read_url(session, url_next[0] + '/' + link['href'])

async def main():
    session = aiohttp.ClientSession()
    await read_url(session, base_url)
    await session.close()
    print(sum(digits))


if __name__ == '__main__':
    asyncio.run(main())