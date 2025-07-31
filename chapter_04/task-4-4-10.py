import asyncio
places = [
    "начинает путешествие",
    "находит загадочный лес",
    "переправляется через реку",
    "встречает дружелюбного дракона",
    "находит сокровище"]

roles = ["Искатель приключений", "Храбрый рыцарь", "Отважный пират"]

async def counter(name, delay=.1):
    for place in places:
        print(f"{name} {place}...")
        await asyncio.sleep(delay)


async def main():
    task1 = asyncio.create_task(counter(roles[0], delay=0.2))
    task2 = asyncio.create_task(counter(roles[1]))
    task3 = asyncio.create_task(counter(roles[2], .3))

    #Дождитесь выполнения всех созданных задач в главной корутине с помощью await.
    await asyncio.gather(task1, task2, task3)

asyncio.run(main())