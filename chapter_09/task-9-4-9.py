"""
Моделирование доступа к базе данных
"""
import asyncio

# Имена пользователей
users = ['Alice', 'Bob', 'Charlie', 'Dave', 'Eva', 'Frank', 'George', 'Helen', 'Ivan', 'Julia']


async def controller(condition: asyncio.Condition):
    async with condition:
        for _ in range(len(users)):
            await asyncio.sleep(.2)
            condition.notify()


async def connect_db(user: str, condition: asyncio.Condition):
    async with condition:
        print(f"Пользователь {user} ожидает доступа к базе данных")
        await condition.wait()
        print(f"Пользователь {user} подключился к БД")
        await asyncio.sleep(.1)
        print(f"Пользователь {user} отключается от БД")


async def main():
    condition = asyncio.Condition()
    tasks_connect = [asyncio.create_task(connect_db(user, condition)) for user in users]
    tasks_controller = asyncio.create_task(controller(condition))
    await asyncio.gather(*tasks_connect, tasks_controller)


asyncio.run(main())
