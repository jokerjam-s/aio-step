"""
Пиротехническое шоу.

Задание: Написать код, который будет моделировать шоу с фейерверками, используя все возможные комбинации форм,
цветов и действий. Каждый фейерверк представляет собой уникальную комбинацию этих характеристик.
Ваша задача - написать асинхронный код, который имитирует запуск каждого фейерверка и затем
выводит сообщение о его завершении.
"""
import asyncio
import itertools
import random

shapes = ["circle", "star", "square", "diamond", "heart"]
colors = ["red", "blue", "green", "yellow", "purple"]
actions = ["change_color", "explode", "disappear"]

combinations = list(itertools.product(shapes, colors, actions))


async def launch_firework(shape, color, action):
    print(f"Запущен {color} {shape} салют, в форме {action}!!!")
    await asyncio.sleep(random.randint(1, 5))
    print(f"Салют {color} {shape} завершил выступление {action}")


async def main():
    async with asyncio.TaskGroup() as tg:
        _ = [tg.create_task(launch_firework(*combination)) for combination in combinations]


asyncio.run(main())
