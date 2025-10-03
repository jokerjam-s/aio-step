import asyncio

async def my_coroutine():
    await asyncio.sleep(1)
    return "Результат выполнения"

async def main():
    # Создаем корутину
    coro = my_coroutine()
    # Создаем задачу из корутины и получаем объект Task
    task = asyncio.create_task(coro)

    # Получаем исходную корутину из задачи
    original_coroutine = task.get_coro()

    print(f"Тип объекта Task: {type(task)}")
    print(f"Тип исходной корутины: {type(original_coroutine)}")
    print(f"Полученная корутина: {original_coroutine}")

    # Запускаем задачу и получаем результат
    result = await task
    print(f"Результат задачи: {result}")

if __name__ == "__main__":
    asyncio.run(main())