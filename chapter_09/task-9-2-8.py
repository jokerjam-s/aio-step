"""
Роботы на складе.
"""

import asyncio

robot_names = ['Электра', 'Механикс', 'Оптимус', 'Симулакр', 'Футуриус']

lock = asyncio.Lock()
place_tap = 0


async def robots_move(name: str, id: int):
    global place_tap
    async with lock:
        print(f"Робот {name}({id}) передвигается к месту A")
        place_tap += 1
        print(f"Робот {name}({id}) достиг места A. Место A посещено {place_tap} раз")


async def main():
    tasks = [asyncio.create_task(robots_move(robot_names[i], i)) for i in range(len(robot_names))]
    await asyncio.gather(*tasks)


asyncio.run(main())