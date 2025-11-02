"""
Простые датчики сигнализации
"""
import asyncio

ip = ["192.168.0.3", "192.168.0.1", "192.168.0.2", "192.168.0.4", "192.168.0.5"]

alarm = asyncio.Event()


async def sensor(number: int):
    print(f"Датчик {number} IP-адрес {ip[number]} настроен и ожидает срабатывания")
    await alarm.wait()
    print(f"Датчик {number} IP-адрес {ip[number]} активирован, \"Wee-wee-wee-wee\"")


async def set_alarm():
    await asyncio.sleep(5)
    alarm.set()
    print("Датчики зафиксировали движение")


async def main():
    tasks = [asyncio.create_task(sensor(i)) for i in range(len(ip))]
    tasks.append(asyncio.create_task(set_alarm()))
    await asyncio.gather(*tasks)


asyncio.run(main())
