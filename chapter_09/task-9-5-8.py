"""
Асинхронный контроллер запросов.
"""
import asyncio
import random

users = ["sasha", "petya", "masha", "katya", "dima", "olya", "igor", "sveta", "nikita", "lena",
         "vova", "yana", "kolya", "anya", "roma", "nastya", "artem", "vera", "misha", "liza"]

sem = asyncio.Semaphore(3)
requests_amount = 0


async def make_request(user: str, sem: asyncio.Semaphore):
    global requests_amount
    async with sem:
        requests_amount += 1
        print(f"Пользователь {user} делает запрос")
        await asyncio.sleep(0)
        print(f"Запрос от пользователя {user} завершен")
        print(f"Всего запросов: {requests_amount}")


async def main():
    tasks = [asyncio.create_task(make_request(user, sem)) for user in users]
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    asyncio.run(main())