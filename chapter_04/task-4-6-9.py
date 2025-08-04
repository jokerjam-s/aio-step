"""
Космические Исследования 3.0
"""
import asyncio
import time

equipment_list = ['#001 ps5f6537c5-506f-43c2-b095-1890ef579c52: 265 units',
                  '#002 ps5ec3020b-022f-466b-845a-a8f11161a6d1: 39 units',
                  '#003 psb5c6c090-4f1a-4741-936e-5fe2b3e8d181: 242 units',
                  '#004 ps10c90127-a4a5-4f85-b23f-66421ab04b09: 108 units',
                  '#005 psa8b77d97-ef82-4832-9601-36abfc399af2: 72 units']


# Корутина для отправки запроса.
async def equipment_request(request: str):
    await asyncio.sleep(1)
    data = request.split()
    return f"{data[0]} os Ok!"


def query_time():
    return time.time()


# Корутина для управления отправкой запросов на заказ оборудования
async def send_requests():
    tasks = [equipment_request(r) for r in equipment_list]
    await asyncio.gather(*tasks)
    waiting_time = query_time()

    print(f"На отправку {len(equipment_list)} запросов потребовалось {round(waiting_time, 6)} секунд!")


asyncio.run(send_requests())
