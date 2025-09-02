"""
Асинхронное сканирование портов/
"""
import asyncio
import random


async def scan_port(address, port):
    await asyncio.sleep(1)
    if random.choice((True, False)):
        print(f"Порт {port} на адресе {address} открыт")
        return port
    return None


async def scan_range(address, start_port, end_port):
    print(f"Сканирование портов с {start_port} по {end_port} на адресе {address}")
    tasks = [asyncio.create_task(scan_port(address, p)) for p in range(start_port, end_port + 1)]
    await asyncio.gather(*tasks)
    open_ports = [t.result() for t in tasks if t.result()]
    if len(open_ports) > 0:
        print(f"Открытые порты на адресе {address}: {open_ports}")
    else:
        print(f"Открытых портов на адресе {address} не найдено")


async def main():
    await scan_range('192.168.0.1', 80, 85)


asyncio.run(main())
