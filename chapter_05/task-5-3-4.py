"""
Симулятор асинхронной загрузки файлов
"""
import asyncio

# Словарь файлов и их размеров
files = {
    "file1.mp4": 32,
    "image2.png": 24,
    "audio3.mp3": 16,
    "document4.pdf": 8,
    "archive5.zip": 40,
    "video6.mkv": 48,
    "presentation7.pptx": 12,
    "ebook8.pdf": 20,
    "music9.mp3": 5,
    "photo10.jpg": 7,
    "script11.py": 3,
    "database12.db": 36,
    "archive13.rar": 15,
    "document14.docx": 10,
    "spreadsheet15.xls": 25,
    "image16.gif": 2,
    "audioBook17.mp3": 60,
    "tutorial18.mp4": 45,
    "code19.zip": 22,
    "profile20.jpg": 9
}


async def download_file(file_name: str, file_size: int, speed: float):
    time_load = round(file_size / speed, 3)
    print(f"Начинается загрузка файла: {file_name}, его размер {file_size} мб, время загрузки составит {time_load} сек")
    await asyncio.sleep(time_load)
    print(f"Загрузка завершена: {file_name}")


async def monitor_tasks(tasks):
    all_done = True
    while all_done:
        all_done = False
        for task in tasks:
            if task.done():
                print(f"Задача {task.get_name()}: завершена, Статус задачи True")
            else:
                print(f"Задача {task.get_name()}: в процессе, Статус задачи False")
                all_done = True
        await asyncio.sleep(0.2)
    print("Все файлы успешно загружены")


async def main():
    tasks = []
    for f, s in files.items():
        task = asyncio.create_task(download_file(f, s, 8))
        task.set_name(f)
        tasks.append(task)

    task_monitor = asyncio.create_task(monitor_tasks(tasks))

    await asyncio.gather(*tasks, task_monitor)

asyncio.run(main())
