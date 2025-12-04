"""
Асинхронный подсчет: Суммирование данных из CSV файлов 5000 файлов
"""
import asyncio
import csv
import json

import aiofiles
import aiocsv
from aiofiles import os as aos

path = './5000csv'

lock = asyncio.Lock()
counter = 0


async def read_info(filename: str):
    global counter
    async with aiofiles.open(f"{path}/{filename}", encoding="utf-8", mode="r", newline="") as f:
        reader = aiocsv.AsyncReader(f)
        async for row in reader:
            async with lock:
                counter += int(row[0])


async def main():
    # counter = 0
    files = await aos.listdir(path)
    tasks = [asyncio.create_task(read_info(f)) for f in files]

    await asyncio.gather(*tasks)

    print(counter)


if __name__ == '__main__':
    asyncio.run(main())
