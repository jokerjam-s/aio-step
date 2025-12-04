import asyncio

from aiofiles import os as aos


async def read_file(filename) -> int:
    with open(filename) as f:
        content = f.read()
    num = int(content)
    return num if num % 2 == 0 else 0


async def main():
    dir_name = './files'

    files = await aos.listdir(dir_name)
    tasks = [asyncio.create_task(read_file(f"./files/{f}")) for f in files]

    await asyncio.gather(*tasks)

    summa = sum([t.result() for t in tasks])
    print(summa)


if __name__ == '__main__':
    asyncio.run(main())
