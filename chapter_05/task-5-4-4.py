"""
Ожидание результата от корутины
"""
import asyncio

async def coroutine():
    await asyncio.sleep(.5)
    return 'code'

async def main():
    task = asyncio.create_task(coroutine())
    await task
    print(task.result())


asyncio.run(main())