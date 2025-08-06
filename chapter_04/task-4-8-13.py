"""
Гонка процессоров
"""
processor_delays = {
    'Intel Core i9-11900K': 7.01,
    'Intel Core i7-11700K': 4.32,
    'Intel Core i5-11600K': 8.59,
    'AMD Ryzen 9 5950X': 2.53,
}

import asyncio


async def simulate_processing(delay):
    await asyncio.sleep(delay)


async def main():
    tasks = [asyncio.create_task(simulate_processing(v), name=k) for k, v in processor_delays.items()]
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)

    print(f"Первый завершенный процесс: {done.pop().get_name()}")

    for task in pending:
        task.cancel()


asyncio.run(main())
