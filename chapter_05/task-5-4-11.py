"""
Обработка исключения.
"""
import asyncio


async def coroutine():
    await asyncio.sleep(.5)
    raise ValueError('Секретный код')


async def main():
    task = asyncio.create_task(coroutine())
    try:
        result = await task
        print(result)
    except Exception as e:
        print(e)


asyncio.run(main())
