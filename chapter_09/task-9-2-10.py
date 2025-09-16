"""
Приложение для мониторинга ракетных запусков. Прерывания (Interrupts).
"""
import asyncio
import random

error = None
count = 0
sek = 0

async def monitor_rocket_launches(interrupt_flag):
    global count
    global error
    global sek

    try:
        # Допишите сюда цикл
        while count < 50:
            print(f"Мониторинг ракетных запусков... (Запуск номер {count} прошёл успешно)")
            await asyncio.sleep(1)
            sek += 1
            count += 1
            error = random.choices([True, None], weights=[25, 75])[0]
            if error:
                break
    finally:
        # Поместите сообщение о завершении мониторинга
        print("Завершение мониторинга ракетных запусков")


async def main():
    global error
    global count
    global sek
    interrupt_flag = asyncio.Event()
    # Создайте Task задачу
    task = asyncio.create_task(monitor_rocket_launches(interrupt_flag))
    # Допишите сюда цикл
    while not interrupt_flag.is_set():
        if count == 50:
            interrupt_flag.set()
        if error:
            print(f"Ошибка при запуске произошла на {sek} секунде =(\n"
                  f"Отмена мониторинга ракетных запусков...")
            interrupt_flag.set()
        await asyncio.sleep(5)

    # Запустите созданную корутину в пункте 2 через await
    await task

if __name__ == "__main__":
    asyncio.run(main())