import asyncio


async def set_future_result(value, delay):
    print(f"Задача начата. Установка результата '{value}' через {delay} секунд.")
    await asyncio.sleep(delay)
    print("Результат установлен.")
    return value


async def create_and_use_future():
    task = asyncio.create_task(set_future_result("Успех", 2))

    task_state = "Завершено" if task.done() else "Ожидание"
    print(f"Состояние Task до выполнения: {task_state}")

    print("Задача запущена, ожидаем завершения...")
    await task

    task_state = "Завершено" if task.done() else "Ожидание"
    print(f"Состояние Task после выполнения: {task_state}")

    return task.result()


async def main():
    result = await create_and_use_future()  # Вызовите и дождитесь необходимую функцию
    print("Результат из Task:", result)


asyncio.run(main())
