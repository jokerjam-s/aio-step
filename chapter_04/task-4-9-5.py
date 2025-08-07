"""
Онлайн кинотеатр
"""
import asyncio


async def upload_file(filename: str, delay: float) -> str:
    await asyncio.sleep(delay)
    return filename


async def main():
    files = {
        "Начало": 4.2,
        "Матрица": 3.8,
        "Аватар": 5.1,
        "Интерстеллар": 2.6,
        "Паразиты": 6.0,
        "Джокер": 4.5,
        "Довод": 3.3,
        "Побег из Шоушенка": 5.4,
        "Криминальное чтиво": 2.9,
        "Форрест Гамп": 5.8
    }

    tasks = [asyncio.create_task(upload_file(k, v)) for k, v in files.items()]

    for task in asyncio.as_completed(tasks):
        filename = await task
        print(f"{filename}: фильм загружен на сервер")


asyncio.run(main())
