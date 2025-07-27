# Counter 1 - имя счётчика
# 13 - максимальное значение для счётчика Counter_1
import asyncio

max_counts = {
    "Counter 1": 13,
    "Counter 2": 7
}

counters = {
    "Counter 1": 0,
    "Counter 2": 0
}


async def counter(counter_name: str, sleep_time: float):
    while max_counts[counter_name] > counters[counter_name]:
        await asyncio.sleep(sleep_time)
        counters[counter_name] += 1
        print(f'{counter_name}: {counters[counter_name]}')


async def main():
    tasks = [
        asyncio.create_task(counter("Counter 1", sleep_time=1)),
        asyncio.create_task(counter("Counter 2", sleep_time=1)),
    ]

    await asyncio.gather(*tasks)


asyncio.run(main())
