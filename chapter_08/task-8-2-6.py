"""
Симуляция очереди пациентов в поликлинике.
"""
# Список вшит в задачу, вставлять его в поле ответа не нужно
patient_info = [
    "Алексей Иванов: Прием для общего осмотра",
    "Мария Петрова: Чистка зубов",
    "Ирина Сидорова: Анализ крови",
    "Владимир Кузнецов: Рентгеновское исследование",
    "Елена Васильева: Вакцинация",
    "Дмитрий Николаев: Выписка рецепта",
    "Светлана Михайлова: Осмотр офтальмолога",
    "Никита Алексеев: Сеанс физиотерапии",
    "Ольга Сергеева: Срочный прием",
    "Анна Жукова: Регулярный контрольный осмотр"
]

import asyncio


async def producer(queue: asyncio.Queue):
    # patient_info = []
    for patient in patient_info:
        await queue.put(patient)
        print(f"Регистратор добавил в очередь: {patient}")
        await asyncio.sleep(0)
    await queue.put(None)


async def consumer(queue: asyncio.Queue):
    while True:
        patient = await queue.get()
        if not patient:
            break
        print(f"Врач принял пациента: {patient}")
        queue.task_done()
        await asyncio.sleep(0)


async def main():
    queue = asyncio.Queue()
    task1 = asyncio.create_task(producer(queue))
    task2 = asyncio.create_task(consumer(queue))
    await asyncio.gather(task1, task2)

asyncio.run(main())
