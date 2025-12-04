"""
Асинхронный подсчет: Суммирование данных из CSV файлов в 5000 подпапках.
"""
import asyncio
from os import DirEntry

import aiocsv
import aiofiles
from aiofiles import os as aos

path = './5000folder'

lock = asyncio.Lock()
counter = 0


async def load_data(file: DirEntry):
    global counter
    async with aiofiles.open(file.path, encoding="utf-8", mode="r", newline="") as f:
        reader = aiocsv.AsyncReader(f)
        async for row in reader:
            async with lock:
                counter += int(row[0])


async def scan_dir(path: str):
    files = []
    dirs = await aos.scandir(path)
    for f in dirs:
        if f.is_dir():
            files += await scan_dir(path + '/' + f.name)
        if f.is_file():
            files.append(f)
    return files


async def main():
    files = await scan_dir(path)
    tasks = [asyncio.create_task(load_data(file)) for file in files]
    await asyncio.gather(*tasks)

    print(counter)


asyncio.run(main())
