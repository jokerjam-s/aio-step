import asyncio

files = ['image.png', 'file.csv', 'file1.txt']  # полный список вшит в задачу


async def download_file(file_name):
    # функция вшита в задачу, ее нужно применить к каждому файлу из files
    # Для некоторых файлов будут сгененрированы исключения
    pass


# ваш код пишите тут:
async def main():
    try:
        async with asyncio.TaskGroup() as tg:
            tasks = [tg.create_task(download_file(f)) for f in files]
    except* FileNotFoundError as e:
        for err in e.exceptions:
            print(err)
    except* PermissionError as e:
        for err in e.exceptions:
            print(err)
    except* TimeoutError as e:
        for err in e.exceptions:
            print(err)


asyncio.run(main())
