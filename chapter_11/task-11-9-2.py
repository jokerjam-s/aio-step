"""
Простая расшифровка
https://asyncio.ru/zadachi/1/index.html
"""
import asyncio

import aiohttp
from bs4 import BeautifulSoup

code_dict = {
    0: 'F',
    1: 'B',
    2: 'D',
    3: 'J',
    4: 'E',
    5: 'C',
    6: 'H',
    7: 'G',
    8: 'A',
    9: 'I'
}

async def decode(code_dict: dict, chifr: str) -> str:
    chars = []
    for c in chifr:
        chars.append(code_dict[int(c)])
    return ''.join(chars)

async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://asyncio.ru/zadachi/1/index.html') as resp:
            soup = BeautifulSoup(await resp.text(), 'html.parser')
            p_text = soup.find('p').text.strip()

    strk = await decode(code_dict, p_text)

    print(strk)


if __name__ == '__main__':
    asyncio.run(main())