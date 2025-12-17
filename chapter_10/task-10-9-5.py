"""
Асинхронное преобразование CSV в JSON
"""
import asyncio
import json

import aiocsv
import aiofiles

csv_file = './file/address_10000.csv'
json_file = './file/address_10000.json'


async def main():
    json_data = []

    async with aiofiles.open(csv_file, encoding='utf-8-sig') as f:
        csv_reader = aiocsv.AsyncDictReader(f, delimiter=';')
        async for row in csv_reader:
            json_data.append(row)

    async with aiofiles.open(json_file, encoding='utf-8', mode="w") as j:
        await j.write(json.dumps(json_data, ensure_ascii=False))


if __name__ == '__main__':
    asyncio.run(main())
