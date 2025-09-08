"""
Марафон компьютерных игр.
"""
import asyncio
from asyncio import LifoQueue


async def autosave(queue: LifoQueue):
    time = 1
    while True:
        print(f"Автосохранение игры через {time} часов")
        await queue.put(f'Автосохранение {time}')
        await asyncio.sleep(.1)
        time += 1
        if time > 20:
            break


async def simulate_gameplay(queue: LifoQueue):
    time = 1
    while True:
        game = await queue.get()
        if time in [5,10,15,20]:
            print(f"Загружена последняя версия игры: {game}")
        time+= 1
        if time > 20:
            break


async def main():
    queue = LifoQueue()
    save = asyncio.create_task(autosave(queue))
    load = asyncio.create_task(simulate_gameplay(queue))
    await asyncio.gather(save, load)
    print('Игра пройдена!')


asyncio.run(main())
