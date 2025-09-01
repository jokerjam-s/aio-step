"""
Наличие товаров на складе.
"""
import asyncio

warehouse_store = {
    "Диван": 15,
    "Обеденный_стол": 10,
    "Офисное_кресло": 25,
    "Кофейный_столик": 12,
    "Кровать": 8,
    "Книжный_шкаф": 20,
    "ТВ-тумба": 7,
    "Шкаф": 9,
    "Письменный_стол": 18,
    "Тумбочка": 14,
    "Комод": 11,
    "Барный_стул": 22,
    "Угловой_диван": 4,
    "Двухъярусная_кровать": 3,
    "Шезлонг": 2,
    "Консольный_столик": 16,
    "Кресло": 17,
    "Туалетный_столик": 19,
    "Книжный_стеллаж": 24,
    "Банкетка": 10,
    "Обеденный_стул": 28,
    "Кресло-качалка": 15,
    "Шкаф-купе": 18,
    "Табуретка": 40,
    "Стеллаж": 13,
    "Кресло-мешок": 5,
    "Кухонный_гарнитур": 6,
    "Журнальный_столик": 8,
    "Витрина": 7,
    "Полка": 30
}

order = {'Диван': 5, 'Обеденный_стол': 3, 'Табуретка': 50, 'Гардероб': 1}

# Товары на складе:
""" warehouse_store = {
    "Диван": 15,
    "Обеденный стол": 10,
    ... }"""


# Заказ:
# order = {...}

# Тут пишите ваш код:
async def check_store(item, quantity):
    count = warehouse_store.get(item, 0)
    current_task = asyncio.current_task()
    if count == 0:
        current_task.set_name(f"Отсутствует: {item}")
    elif count < quantity:
        current_task.set_name(f"Частично в наличии: {item}")
    else:
        current_task.set_name(f"В наличии: {item}")


async def main():
    tasks = [asyncio.create_task(check_store(k, v)) for k, v in order.items()]
    await asyncio.gather(*tasks)
    task_names = [t.get_name() for t in tasks]
    task_names.sort()

    for t in task_names:
        print(t)


asyncio.run(main())
