"""
Назначение callback-функций в зависимости от поведения задачи.
"""
import asyncio
import random
from asyncio import Task

random.seed(5)

def on_data_parsed(task: Task):
    result = task.result()
    print(f"Найдено {len(result)} файлов для скачивания: {result}")


async def parse_data(url):
    await asyncio.sleep(1)
    if random.choice([True, False]):
        file_urls = [f"{url}/example_file.zip"]
        asyncio.current_task().add_done_callback(on_data_parsed)
    else:
        file_urls = []
    return file_urls


async def main():
    urls = [
        "https://example.com/data1",
        "https://example.com/data2",
        "https://example.com/data3"
    ]
    tasks = [asyncio.create_task(parse_data(url)) for url in urls]
    await asyncio.wait(tasks)

asyncio.run(main())