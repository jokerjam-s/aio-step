"""
Нужно больше золота
"""
import asyncio
import random

# Не менять!
random.seed(1)


async def collect_gold():
    await asyncio.sleep(random.randint(1, 5))
    return random.randint(10, 50)


async def main():
    total_gold = 0
    tasks = [asyncio.create_task(collect_gold()) for _ in range(10)]

    for task in asyncio.as_completed(tasks):
        amount = await task
        total_gold += amount
        print(f"Собрано {amount} единиц золота.")
        print(f"Общее количество золота: {total_gold} единиц.")
        print()


asyncio.run(main())
