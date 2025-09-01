"""
Асинхронная загрузка с серверов.

Создайте пять задач (по одной на каждый сервер), которые работали бы конкурентно и
загружали данные из разных серверов в базу данных. В качестве имитации загрузки данных с серверов используйте
асинхронную функцию sleep. Пусть каждая задача засыпает на случайное значение от 0 до 5, имитируя запрос к базе данных.
"""
import asyncio
import random

server_names = {
    "1": "Server_Alpha",
    "2": "Server_Beta",
    "3": "Server_Gamma",
    "4": "Server_Delta",
    "5": "Server_Epsilon",
}


async def load_data(server):
    print(f"Загрузка данных с сервера {server} началась")
    await asyncio.sleep(random.randint(1, 5))
    print(f"Загрузка данных с сервера {server} завершена")


async def main():
    tasks = [asyncio.create_task(load_data(server_names[str(n)])) for n in range(1, 6)]
    await asyncio.gather(*tasks)


asyncio.run(main())
