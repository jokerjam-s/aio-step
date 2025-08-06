"""
Гастрономический марафон
"""
dishes = {
    'Куриный суп': 118,
    'Бефстроганов': 13,
    'Рататуй': 49,
    'Лазанья': 108,
    'Паэлья': 51,
    'Утка по-пекински': 41,
}

import asyncio


async def cook_dish(name, duration):
    print(f"Приготовление {name} начато.")
    await asyncio.sleep(duration / 10)
    print(f"Приготовление {name} завершено. за {duration / 10}")


async def main():
    tasks = [asyncio.create_task(cook_dish(k, v), name=k) for k, v in dishes.items()]
    done, pending = await asyncio.wait(tasks, timeout=10)

    for task in pending:
        print(f"{task.get_name()} не успел(а,о) приготовиться и будет отменено.")
        task.cancel()

    print(f"\nПриготовлено блюд: {len(done)}. Не успели приготовиться: {len(pending)}.")


asyncio.run(main())
