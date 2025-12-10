"""
Цифровые следы
"""
from datetime import datetime
import json
from asyncio import Task

import aiocsv
import aiofiles
from aiofiles import os as aos
import asyncio

sem = asyncio.BoundedSemaphore(1000)
data = []
data_lock = asyncio.Lock()


async def scan_json(json_file: str):
    async with sem:
        try:
            # Используем aiofiles.open для асинхронного открытия файла
            async with aiofiles.open(json_file, mode='r', encoding='utf-8') as f:
                content = await f.read()  # Асинхронное чтение всего содержимого
                async with data_lock:
                    content_ = json.loads(content)
                    data.extend([c for c in content_ if c["HTTP-статус"] == 200])  # Синхронное преобразование строки в объект
        except FileNotFoundError:
            print(f"Ошибка: Файл не найден по пути {json_file}")
            return None
        except json.JSONDecodeError:
            print(f"Ошибка: Некорректный формат JSON в файле {json_file}")
            return None


async def scan_dir(path: str, tasks: list[Task] = None):
    if tasks is None:
        tasks = []
    dirs = await aos.scandir(path)
    for f in dirs:
        if f.is_dir():
            await scan_dir(path + '/' + f.name, tasks)
        if f.is_file():
            tasks.append(asyncio.create_task(scan_json(path + '/' + f.name)))
    return tasks


async def main():
    tasks = await scan_dir('./logs')
    await asyncio.gather(*tasks)

    for d in data:
        d['Время и дата'] = datetime.strptime(d['Время и дата'], "%Y-%m-%d %H:%M:%S")


    sorted_data = sorted(data, key=lambda item: item['Время и дата'])

    async with aiofiles.open('./data.csv', mode='w', encoding='utf-8-sig', newline='') as f:
        writer = aiocsv.AsyncDictWriter(f, delimiter=';', dialect='excel',
                                        fieldnames=["Время и дата", "IP-адрес", "User-Agent", "Запрошенный URL",
                                                    "HTTP-статус", "Реферер", "Cookie",
                                                    "Размер страницы и заголовки ответа", "Метод запроса",
                                                    "Информация об ошибке"],
                                        lineterminator='\n')
        await writer.writeheader()
        for i in sorted_data:
            i['Время и дата'] = i['Время и дата'].strftime("%d.%m.%Y %H:%M:%S")
            await writer.writerow(i)


if __name__ == '__main__':
    asyncio.run(main())
