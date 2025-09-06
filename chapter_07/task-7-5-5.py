"""
Почините код 1.0
"""
import asyncio


async def coro(num):
    await asyncio.sleep(num * 0.1)
    print(f'Задача {num} выполнена')


async def main():
    tasks = [asyncio.create_task(coro(i)) for i in range(5)]
    await asyncio.gather(*tasks)
    print('Работа программы завершена')


asyncio.run(main())