"""
Асинхронный Web-сканер статусов
"""
import asyncio

import aiohttp

sem = asyncio.Semaphore(10)
status_codes = []


async def get_digit(url: str):
    async with sem:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                status_codes.append(resp.status)


async def main():
    tasks = [asyncio.create_task(get_digit(f"https://asyncio.ru/zadachi/5/{i}.html")) for i in range(1, 1001)]
    await asyncio.gather(*tasks)

    num = sum(status_codes)
    print(num)


if __name__ == '__main__':
    asyncio.run(main())
