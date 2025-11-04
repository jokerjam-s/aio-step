"""
Поиск квартир.
"""
import asyncio

apartments_data = [
    {"id": "apt_1_1", "price": 45000, "rooms": 2, "address": "ул. Ленина, д. 10", "area": 50},
    {"id": "apt_1_2", "price": 55000, "rooms": 3, "address": "ул. Пушкина, д. 15", "area": 75},
    {"id": "apt_1_3", "price": 50000, "rooms": 2, "address": "ул. Суворова, д. 8", "area": 55},
    {"id": "apt_1_4", "price": 65000, "rooms": 3, "address": "ул. Чехова, д. 22", "area": 80},
    {"id": "apt_1_5", "price": 48000, "rooms": 2, "address": "ул. Горького, д. 12", "area": 52},
    {"id": "apt_2_2", "price": 60000, "rooms": 4, "address": "ул. Чайковского, д. 20", "area": 90},
    {"id": "apt_2_3", "price": 37000, "rooms": 1, "address": "ул. Тургенева, д. 9", "area": 42},
    {"id": "apt_2_4", "price": 62000, "rooms": 3, "address": "ул. Арбат, д. 25", "area": 85},
    {"id": "apt_2_5", "price": 33000, "rooms": 1, "address": "ул. Шолохова, д. 7", "area": 38},
    {"id": "apt_3_1", "price": 70000, "rooms": 4, "address": "ул. Тверская, д. 3", "area": 95},
    {"id": "apt_3_2", "price": 72000, "rooms": 3, "address": "ул. Кутузовский проспект, д. 21", "area": 100},
    {"id": "apt_3_3", "price": 75000, "rooms": 4, "address": "ул. Неглинная, д. 11", "area": 110},
    {"id": "apt_3_4", "price": 69000, "rooms": 3, "address": "ул. Новослободская, д. 14", "area": 90},
    {"id": "apt_3_5", "price": 71000, "rooms": 3, "address": "ул. Большая Дмитровка, д. 17", "area": 95},
    {"id": "apt_4_1", "price": 40000, "rooms": 2, "address": "ул. Ярославская, д. 30", "area": 50},
    {"id": "apt_4_2", "price": 42000, "rooms": 2, "address": "ул. Лескова, д. 6", "area": 52},
    {"id": "apt_4_3", "price": 43000, "rooms": 2, "address": "ул. Синельникова, д. 5", "area": 54},
    {"id": "apt_4_4", "price": 44000, "rooms": 2, "address": "ул. Петровка, д. 28", "area": 56},
    {"id": "apt_4_5", "price": 41000, "rooms": 2, "address": "ул. Колобова, д. 4", "area": 51},
    {"id": "apt_5_1", "price": 55000, "rooms": 3, "address": "ул. Авиамоторная, д. 12", "area": 70},
    {"id": "apt_5_2", "price": 56000, "rooms": 3, "address": "ул. Вавилова, д. 19", "area": 72},
    {"id": "apt_5_3", "price": 57000, "rooms": 3, "address": "ул. Керченская, д. 8", "area": 74},
    {"id": "apt_5_4", "price": 58000, "rooms": 3, "address": "ул. Профсоюзная, д. 16", "area": 76},
    {"id": "apt_5_5", "price": 59000, "rooms": 3, "address": "ул. Синельникова, д. 10", "area": 78},
    {"id": "apt_2_1", "price": 35000, "rooms": 1, "address": "ул. Гагарина, д. 5", "area": 40},
]

# Тут создавайте объект семафора
semaphore = asyncio.BoundedSemaphore(value=5)


async def fetch_apartment_data(min: int, max: int, rooms: int, flat: dict):
    async with semaphore:
        await asyncio.sleep(1)
        if min <= flat["price"] <= max and rooms == flat["rooms"]:
            print(flat)


async def main():
    params = input()
    data = params.split()

    min_price = int(data[0])
    max_price = int(data[1])
    rooms_amount = int(data[2])

    tasks = [asyncio.create_task(fetch_apartment_data(min_price, max_price, rooms_amount, a)) for a in apartments_data]

    await asyncio.gather(*tasks)


asyncio.run(main())
