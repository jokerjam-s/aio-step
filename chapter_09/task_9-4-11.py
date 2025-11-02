"""
Крафтим в три цеха.
"""
import asyncio

stone_amount = 0
metal_amount = 0
cloth_amount = 0

stone_condition = asyncio.Condition()
metal_condition = asyncio.Condition()
cloth_condition = asyncio.Condition()

stop_stone = asyncio.Event()
stop_metal = asyncio.Event()
stop_cloth = asyncio.Event()


stone_resources_dict = {
    'Каменная плитка': 10,
    'Каменная ваза': 40,
    'Каменный столб': 50,
}

metal_resources_dict = {
    'Металлическая цепь': 6,
    'Металлическая рамка': 24,
    'Металлическая ручка': 54,
}

cloth_resources_dict = {
    'Тканевая занавеска': 8,
    'Тканевый чехол': 24,
    'Тканевое покрывало': 48,
}

condition = asyncio.Condition()


async def gather_stone():
    global stone_amount
    # Добываем камень, 10ед каждую сек.
    while not stop_stone.is_set():
        async with stone_condition:
            await asyncio.sleep(1)
            stone_amount += 10
            print(f"Добыто 10 ед. камня. На складе {stone_amount} ед.")
            stone_condition.notify()
        await asyncio.sleep(0)


async def gather_metal():
    # Добываем металл, 6ед каждую сек.
    global metal_amount
    while not stop_metal.is_set():
        async with metal_condition:
            await asyncio.sleep(1)
            metal_amount += 6
            print(f"Добыто 6 ед. металла. На складе {metal_amount} ед.")
            metal_condition.notify()
        await asyncio.sleep(0)


async def gather_cloth():
    # Добываем ткань, 8ед каждую сек.
    global cloth_amount
    while not stop_cloth.is_set():
        async with cloth_condition:
            await asyncio.sleep(1)
            cloth_amount += 8
            print(f"Добыто 8 ед. ткани. На складе {cloth_amount} ед.")
            cloth_condition.notify()
        await asyncio.sleep(0)


async def craft_stone_items(items: dict):
    # Мастерская по крафту из камня
    global stone_amount
    async with stone_condition:
        for key, value in items.items():
            while value > stone_amount:
                await stone_condition.wait()
            print(f"Изготовлен {key} из камня.")
            stone_amount -= value
        stop_stone.set()


async def craft_metal_items(items: dict):
    # Мастерская по крафту из металла
    global metal_amount
    async with metal_condition:
        for key, value in items.items():
            while value > metal_amount:
                await metal_condition.wait()
            print(f"Изготовлен {key} из металла.")
            metal_amount -= value
        stop_metal.set()


async def craft_cloth_items(items: dict):
    # Мастерская по крафту из ткани
    global cloth_amount
    async with cloth_condition:
        for key, value in items.items():
            while value > cloth_amount:
                await cloth_condition.wait()
            print(f"Изготовлен {key} из ткани.")
            cloth_amount -= value
        stop_cloth.set()


async def main():
    # Запускаем производства
    tasks = [
        asyncio.create_task(gather_stone()),
        asyncio.create_task(gather_metal()),
        asyncio.create_task(gather_cloth()),
        asyncio.create_task(craft_stone_items(stone_resources_dict)),
        asyncio.create_task(craft_metal_items(metal_resources_dict)),
        asyncio.create_task(craft_cloth_items(cloth_resources_dict)),
    ]
    await asyncio.gather(*tasks)


asyncio.run(main())
