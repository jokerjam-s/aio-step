import asyncio


async def cor(i: int):
    await asyncio.sleep(1 / i)
    print(f'Coroutine {i} is done')


async def main():
    tasks = []

    for i in range(1, 4):
        tasks.append(asyncio.create_task(cor(i)))
    await asyncio.gather(*tasks)


asyncio.run(main())
