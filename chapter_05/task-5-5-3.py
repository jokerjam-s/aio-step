"""
Идентификатор задач.
"""
import asyncio

async def process_task():
    await asyncio.sleep(1)
    return id(asyncio.current_task())

async def main():
    tasks = [asyncio.create_task(process_task()) for _ in range(10)]
    results = await asyncio.gather(*tasks)
    print(results)


asyncio.run(main())