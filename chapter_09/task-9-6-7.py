"""
Премиум аккаунт vs бесплатный доступ.
"""
import asyncio


async def convert_file(filename: str, semaphore: asyncio.BoundedSemaphore) -> str:
    try:
        await semaphore.acquire()
        await asyncio.sleep(1)
        return f"Файл {filename} обработан"
    except:
        raise
    finally:
        semaphore.release()


async def main():
    files = input()
    mode = input()
    data = files.split()

    if mode == "free":
        semaphore = asyncio.BoundedSemaphore(2)
    else:
        semaphore = asyncio.BoundedSemaphore(10)

    tasks = [asyncio.create_task(convert_file(f, semaphore)) for f in data]
    await asyncio.gather(*tasks)

    for t in tasks:
        print(t.result())


asyncio.run(main())
