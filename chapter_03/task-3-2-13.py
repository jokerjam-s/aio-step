import asyncio


async def generate(num: int):
    await asyncio.sleep(0.1)
    print(f"Корутина generate с аргументом {num}")


async def main():
    for i in range(10):
        await generate(i)


asyncio.run(main())
