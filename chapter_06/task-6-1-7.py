"""
Пользовательский менеджер контекста.
"""
import asyncio

# База данных
database = [
    {"название": "Разработать API", "статус": "Завершена"},
    {"название": "Написать документацию", "статус": "Ожидает"},
    {"название": "Провести код-ревью", "статус": "Ожидает"}
]


# Не менять
class AsyncListManager:
    async def __aenter__(self):
        await self.connect()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.disconnect()

    async def connect(self):
        print("Начало работы с базой данных")
        await asyncio.sleep(0.5)

    async def disconnect(self):
        print("Завершение работы с базой данных")
        await asyncio.sleep(0.5)

    async def stage_append(self, value):
        await asyncio.sleep(1)
        database.append(value)
        print('Новые данные добавлены')


# Тут пишите ваш код
async def main():
    async with AsyncListManager() as am:
        await am.stage_append({'название': 'Настроить CI/CD', 'статус': 'В процессе'})
        for data in database:
            print(data)


asyncio.run(main())
