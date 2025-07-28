"""
Отмена и проверка отмены Task/Future
"""

import asyncio


async def async_operation():
    print("Начало асинхронной операции.")
    try:
        await asyncio.sleep(2)
        print("Асинхронная операция успешно завершилась.")
    except asyncio.CancelledError:
        print("Асинхронная операция была отменена в процессе выполнения.")
        raise


async def main():
    print("Главная корутина запущена.")

    task = asyncio.create_task(async_operation())
    await asyncio.sleep(0.1)

    print("Попытка отмены Task.")
    task.cancel()
    try:
        print("Результат Task:", await task)
    except asyncio.CancelledError:
        print("Обработка исключения: Task был отменен.")

    if task.cancelled():
        print("Проверка: Task был отменен.")
    else:
        print("Проверка: Task не был отменен.")

    print("Главная корутина завершена.")


asyncio.run(main())
