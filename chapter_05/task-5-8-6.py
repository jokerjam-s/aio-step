"""
Поиск отсутствующих файлов.
"""
import asyncio

files = ['image.png', 'file.csv', 'file1.txt' ]
missed_files = ['file.csv']

# Не менять функцию
async def download_file(file_name):
    await asyncio.sleep(1)
    if file_name in missed_files:
        raise FileNotFoundError(f'Файл {file_name} не найден')
    else:
        await asyncio.sleep(1)
        return f'Файл {file_name} успешно скачан'

# Ваш код пишите тут:
async def main():
    tasks = [asyncio.create_task(download_file(f)) for f in files]
    await asyncio.gather(*tasks, return_exceptions=True)

    for t in tasks:
        if t.exception():
            print(t.exception())


asyncio.run(main())