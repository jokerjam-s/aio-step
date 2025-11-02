"""
Крафтим из древесины.
"""
import asyncio

wood_resources_dict = {
    'Деревянный меч': 6,
    'Деревянный щит': 12,
    'Деревянный стул': 24,
}

storage: int = 0
condition = asyncio.Condition()
stop_event = asyncio.Event()
item_ready: int = 0


async def gather_wood():
    # Код по добыче 2 единиц древесины в секунду
    global storage
    while not stop_event.is_set():
        async with condition:
            await asyncio.sleep(1)
            storage += 2
            print(f"Добыто 2 ед. дерева. На складе {storage} ед.")
            condition.notify_all()


async def craft_item(item, count):
    global storage, item_ready
    # Код по изготовлению деревянных предметов
    async with condition:
        while True:
            await condition.wait()
            if storage == count:
                storage -= count
                print(f"Изготовлен {item}.")
                item_ready += 1
                break


async def main():
    storage_task = asyncio.create_task(gather_wood())
    tasks = [asyncio.create_task(craft_item(item, count)) for item, count in wood_resources_dict.items()]
    await asyncio.sleep(0)
    while True:
        await asyncio.sleep(0.9)
        if item_ready == len(wood_resources_dict):
            stop_event.set()
            break


asyncio.run(main())
