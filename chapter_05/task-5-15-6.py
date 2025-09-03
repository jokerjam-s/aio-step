"""
Асинхронное сканирование портов 2.
"""
import asyncio
import random

ip_dct = {'192.168.0.1': [0, 100], '192.168.0.2': [225, 300], '192.168.2.5': [150, 185]}


async def scan_port(address, port):
    """
    Асинхронная функция, имитирующая сканирование порта на заданном ip-адресе.
    """
    await asyncio.sleep(1)
    if random.randint(0, 100) == 1:
        # Печать сообщения об обнаружении открытого порта.
        print(f"Port {port} on {address} is open")
        return port
    return None


async def scan_range(address, start_port, end_port):
    """
    Асинхронная функция, проверяющая состояние диапазона портов по указанному адресу.
    """
    # Печать сообщения о начале сканирования диапазона портов для заданного ip-адреса.
    print(f"Scanning ports {start_port}-{end_port} on {address}")
    check_ports_tasks = [asyncio.create_task(scan_port(address, port)) for port in range(start_port, end_port + 1)]
    await asyncio.gather(*check_ports_tasks)
    return address, [port.result() for port in check_ports_tasks if port.result() is not None]


async def main(dct: dict):
    """
    Основная асинхронная функция, управляющая процессом сканирования портов из переданного в нее словаря.
    """
    tasks = [asyncio.create_task(scan_range(k, v[0], v[1])) for k, v in dct.items()]
    await asyncio.gather(*tasks)
    for t in tasks:
        ports_info = t.result()
        if len(ports_info[1]) > 0:
            print(f"Всего найдено открытых портов {len(ports_info[1])} {ports_info[1]} для ip: {ports_info[0]}")


# Запуск асинхронного приложения с передачей в main() словаря ip_dct
asyncio.run(main(ip_dct))
