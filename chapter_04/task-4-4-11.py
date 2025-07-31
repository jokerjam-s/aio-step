"""
Напишите асинхронный код, который запускает два таймера обратного отсчета с разным временем и названиями.
    Один таймер - это "Квест на поиск сокровищ", который длится 10 секунд.
    Второй - "Побег от дракона", на выполнение которого дается 5 секунд.
Используйте asyncio.create_task() для запуска каждого таймера. Таймер должен выводить оставшееся время в сообщениях
"""
import asyncio


async def countdown(name, seconds):
    for i in range(seconds, 0, -1):
        if name == 'Квест на поиск сокровищ':
            print(f"{name}: Осталось {i} сек. Найди скрытые сокровища!")
        else:
            print(f"{name}: Осталось {i} сек. Беги быстрее, дракон на хвосте!")
        await asyncio.sleep(1)
    print(f"{name}: Задание выполнено! Что дальше?")


async def main():
    treasure_hunt = asyncio.create_task(countdown("Квест на поиск сокровищ", 10))
    dragon_escape = asyncio.create_task(countdown("Побег от дракона", 5))

    await asyncio.gather(treasure_hunt, dragon_escape)


asyncio.run(main())
