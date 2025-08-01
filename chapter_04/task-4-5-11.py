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


async def recharge_portal(x: float) -> float:
    """
    Подзарядка
    :param x: время зарядки
    :return:
    """
    print(f"Подзарядка портала, требуется времени: {x} единиц")
    await asyncio.sleep(x)
    return x * 3


async def check_portal_stability(x: float) -> float:
    """
    Проверка стабильности
    :param x:
    :return:
    """
    print(f"Проверка стабильности портала, требуется времени: {x} единиц")
    await asyncio.sleep(x)
    return x + 4


async def restore_portal(x: float) -> float:
    """
    Восстановление
    :param x:
    :return:
    """
    print(f"Восстановление портала, требуется времени: {x} единиц")
    await asyncio.sleep(x)
    return x * 5


async def close_portal(x: float) -> float:
    """
    Закрытие
    :param x:
    :return:
    """
    print(f"Закрытие портала, требуется времени: {x} единиц")
    await asyncio.sleep(x)
    return x - 1


async def portal_operator():
    task_activate = asyncio.ensure_future(activate_portal(2))
    result_activate = await task_activate
    task_teleport = asyncio.ensure_future(perform_teleportation(3))
    task_recharge = asyncio.ensure_future(recharge_portal(4))
    task_check = asyncio.ensure_future(check_portal_stability(5))
    task_restore = asyncio.ensure_future(restore_portal(6))

    results = await asyncio.gather(task_teleport, task_recharge, task_check, task_restore)

    task_close = asyncio.ensure_future(close_portal(7))
    result_close = await task_close

    print(f"Результат активации портала: {result_activate} единиц энергии")
    print(f"Результат телепортации: {results[0]} единиц времени")
    print(f"Результат подзарядки портала: {results[1]} единиц энергии")
    print(f"Результат проверки стабильности: {results[2]} единиц времени")
    print(f"Результат восстановления портала: {results[3]} единиц энергии")
    print(f"Результат закрытия портала: {result_close} единиц времени")


asyncio.run(portal_operator())
