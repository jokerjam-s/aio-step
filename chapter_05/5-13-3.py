# Время доставки до разных городов:
import asyncio

delivery_times = {
    'Москва': 1,
    'Санкт-Петербург': 3,
    'Новосибирск': 7,
    'Екатеринбург': 5,
    'Нижний Новгород': 4,
    'Челябинск': 6,
    'Омск': 7,
    'Красноярск': 8,
    'Владивосток': 9,
    'Хабаровск': 9
}

# Заказы:
orders = [(подарок, город, пометка), ...]

# Время до нового года:
days_left = 5

# Тут пишите ваш код:
async def deliver(order):
    item = order[0]
    city = order[1]
    await asyncio.sleep(delivery_times[city])
    print(f'Подарок {item} успешно доставлен в г. {city}')

async def main():
    tasks = [asyncio.create_task(deliver(order)) for order in orders if order[2] != "важно"]
    tasks.extend([asyncio.shield(deliver(order)) for order in orders if order[2] == "важно"])
    done, pending = await asyncio.wait(tasks, timeout=days_left, return_when=asyncio.FIRST_EXCEPTION)

    for task in pending:
        task.cancel()

    await asyncio.sleep(max(delivery_times.values()))

asyncio.run(main())