"""
Асинхронный аудит автомобильных складов
"""
import asyncio
import json
from asyncio import Task

import aiocsv
import aiofiles
from aiofiles import os as aos

cost_new = 0
cost_used = 0

cost_calc_new = asyncio.Lock()
cost_calc_used = asyncio.Lock()

sem = asyncio.BoundedSemaphore(1000)


async def scan_csv(filename: str):
    global cost_used, cost_new

    async with sem:
        async with aiofiles.open(filename, encoding='cp1251') as csv_file:
            reader = aiocsv.AsyncDictReader(csv_file, delimiter=';')
            async for row in reader:
                try:
                    if row.get("Состояние авто").upper() == "Б/У":
                        async with cost_calc_used:
                            cost_used += int(row.get("Стоимость авто"))
                    else:
                        async with cost_calc_new:
                            cost_new += int(row.get("Стоимость авто"))
                except Exception as e:
                    print(filename)
                    print(e)


async def scan_dir(path: str, tasks: list[Task] = None):
    if tasks is None:
        tasks = []
    dirs = await aos.scandir(path)
    for f in dirs:
        if f.is_dir():
            await scan_dir(path + '/' + f.name, tasks)
        if f.is_file():
            tasks.append(asyncio.create_task(scan_csv(path + '/' + f.name)))
    return tasks


async def main():
    tasks_csv = await scan_dir("./Задача 3")
    await asyncio.gather(*tasks_csv)

    result = {
        "Б/У": cost_used,
        "Новый": cost_new,
    }
    json.dump(result, open('result.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=4)


if __name__ == '__main__':
    asyncio.run(main())
