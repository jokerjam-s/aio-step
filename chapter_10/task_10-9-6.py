"""
Поиск отличников
"""
import asyncio
import csv
import json

import aiocsv
import aiofiles
from aiofiles import os as aos

path_dir = './tasks'
sem = asyncio.BoundedSemaphore(1000)
dir_loaded = asyncio.Event()
students = []


async def scan_dir(path: str, files: list = None):
    if files is None:
        files = []
    dirs = await aos.scandir(path)
    for f in dirs:
        if f.is_dir():
            await scan_dir(path + '/' + f.name, files)
        if f.is_file():
            files.append(path + '/' + f.name)
    return files


async def scan_csv(filename: str):
    async with sem:
        async with aiofiles.open(filename, encoding='utf-8-sig') as csv_file:
            reader = aiocsv.AsyncDictReader(csv_file)
            async for row in reader:
                if row.get("Балл ЕГЭ") == "100":
                    students.append(row)
                    print(len(students))


async def main():
    data_files = await scan_dir(path_dir)
    print(data_files)
    tasks = [asyncio.create_task(scan_csv(file)) for file in data_files]
    await asyncio.gather(*tasks)

    students.sort(key=lambda x: x['Телефон для связи'])
    json.dump(students, open('students.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=4)


if __name__ == '__main__':
    asyncio.run(main())
