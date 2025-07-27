# Counter 1 - имя счётчика
# 13 - максимальное значение для счётчика Counter_1
import asyncio

max_counts = {
    "Counter 1": 10,
    "Counter 2": 5,
    "Counter 3": 15
}

counters = {
    "Counter 1": 0,
    "Counter 2": 0,
    "Counter 3": 0
}

delays = {
    "Counter 1": 1,
    "Counter 2": 2,
    "Counter 3": 0.5
}

async def counter(counter_name: str):
    while max_counts[counter_name] > counters[counter_name]:
        await asyncio.sleep(delays[counter_name])
        counters[counter_name] += 1
        print(f'{counter_name}: {counters[counter_name]}')


async def main():
    tasks = [asyncio.create_task(counter(key)) for key in max_counts.keys()]
    await asyncio.gather(*tasks)


asyncio.run(main())
