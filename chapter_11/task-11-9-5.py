"""
Спасение презентации: Асинхронная загрузка галереи изображений
"""
import asyncio
import os
import random

import aiofiles
import aiohttp
from bs4 import BeautifulSoup

img_path = "./img/"
url = "https://asyncio.ru/zadachi/4/index.html"
sem = asyncio.Semaphore(50)
file_no = 0

async def load_img(img, session):
    global file_no
    # Создаем имя файла
    file_no += 1
    filename = f"{img_path}image_{file_no}.jpg"

    async with sem:
        async with session.get(img) as response:
            async with aiofiles.open(filename, mode="wb") as img_file:
                await img_file.write(await response.read())


def get_folder_size(folder_path):
    total_size = 0
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            total_size += os.path.getsize(file_path)
    return total_size


async def main():
    img_urls = []

    session = aiohttp.ClientSession()
    response = await session.get(url)
    if response.status == 200:
        soup = BeautifulSoup(await response.text(), 'html.parser')
        main_tag = soup.find('main')
        img_tags = main_tag.find_all('img')
        img_urls = [img['src'] for img in img_tags]


    base_url = url.rsplit('/', 1)[0]
    tasks = [(asyncio.create_task(load_img(base_url + '/' + img_url, session))) for img_url in img_urls]
    await asyncio.gather(*tasks)
    await session.close()
    print(get_folder_size(img_path))


if __name__ == '__main__':
    asyncio.run(main())
