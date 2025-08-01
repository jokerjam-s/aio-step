"""
Написать асинхронный код, который будет имитировать процесс активации портала и последующую телепортацию.
Каждая операция требует определенного времени и выделяет или использует определенное количество единиц энергии.
"""
import asyncio


async def activate_portal(x: float) -> float:
    """
    Активация портала
    :param x: время на активацию
    :return: кол-во энергии необходимой для активации
    """
    print(f"Активация портала в процессе, требуется времени: {x} единиц")
    await asyncio.sleep(x)
    return x * 2


async def perform_teleportation(x: float) -> float:
    """
    Телепорт
    :param x: время для телепортации
    :return: использовано времени
    """
    print(f"Телепортация в процессе, требуется времени: {x} единиц")
    await asyncio.sleep(x)
    return x + 2


async def portal_operator():
    task_activate = asyncio.ensure_future(activate_portal(2))
    activate_result = await task_activate
    task_teleport = asyncio.ensure_future(perform_teleportation(activate_result))
    teleport_result = await task_teleport

    print(f"Результат активации портала: {activate_result} единиц энергии")
    print(f"Результат телепортации: {teleport_result} единиц времени")


asyncio.run(portal_operator())
