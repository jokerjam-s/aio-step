"""
Поиск корректных URL адресов.
"""
import asyncio

# url_list = [...] вшит в задачу.
url_list = []


# Асинхронная функция, проверяющая валидность URL и скачивающая данные - ее писать не надо, она вшита в задачу!
async def check_url(url):
    pass


# ваш код пишите тут:
async def main():
    tasks = [asyncio.create_task(check_url(u), name=u) for u in url_list]
    await asyncio.sleep(1)
    print(len(asyncio.all_tasks()) - 1)


asyncio.run(main())
