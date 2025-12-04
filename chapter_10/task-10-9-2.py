import asyncio
import json

import aiofiles
from aiofiles import os as aos

path = './chat'

lock = asyncio.Lock()


async def read_info(payments: dict, filename: str):
    async with aiofiles.open(f"{path}/{filename}", encoding="utf-8", mode="r") as f:
        stk = await f.readlines()

    for s in stk:
        data = s[22:].split(": ")
        async with lock:
            payments[data[0]] = payments.setdefault(data[0], 0) + len(data[1][:-1])


async def main():
    files = await aos.listdir(path)
    # files = ["chat_1.txt", "chat_2.txt", "chat_3.txt"]
    info = dict()

    tasks = [asyncio.create_task(read_info(info, f)) for f in files]
    await asyncio.gather(*tasks)

    info = dict(sorted(info.items(), key=lambda x: x[1], reverse=True))

    for i in info:
        info[i] = f"{round(info[i] * .03, 2)}р"

    json_info = json.dumps(info, indent=4, ensure_ascii=False)
    print(json_info)


if __name__ == '__main__':
    asyncio.run(main())
