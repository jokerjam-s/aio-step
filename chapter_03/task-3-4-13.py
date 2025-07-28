"""
Последовательное выполнение задач с зависимостями от других задач.
"""
import asyncio


async def first_function(x: int) -> int:
    print(f"Выполняется первая функция с аргументом {x}")
    await asyncio.sleep(1)
    result = x + 1
    print(f"Первая функция завершилась с результатом {result}")
    return result


async def second_function(x: int) -> int:
    print(f"Выполняется вторая функция с аргументом {x}")
    await asyncio.sleep(1)
    result = x * 2
    print(f"Вторая функция завершилась с результатом {result}")
    return result


async def third_function(x: int) -> int:
    print(f"Выполняется третья функция с аргументом {x}")
    await asyncio.sleep(1)
    result = x + 3
    print(f"Третья функция завершилась с результатом {result}")
    return result


async def fourth_function(x: int) -> int:
    print(f"Выполняется четвертая функция с аргументом {x}")
    await asyncio.sleep(1)
    result = x ** 2
    print(f"Четвертая функция завершилась с результатом {result}")
    return result


async def main():
    print("Начало цепочки асинхронных вызовов")

    task_first = asyncio.create_task(first_function(1))
    task_second = asyncio.create_task(second_function(await task_first))
    task_third = asyncio.create_task(third_function(await task_second))
    task_fourth = asyncio.create_task(fourth_function(await task_third))
    final_result = await task_fourth

    print(f"Конечный результат цепочки вызовов: {final_result}")


asyncio.run(main())
