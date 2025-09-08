"""
Координация приема пациентов по специализациям врачей.
"""

patient_info = [
    {'name': 'Алексей Иванов', 'direction': 'Терапевт', 'procedure': 'Прием для общего осмотра'},
    {'name': 'Мария Петрова', 'direction': 'Хирург', 'procedure': 'Малая операция'},
    {'name': 'Ирина Сидорова', 'direction': 'ЛОР', 'procedure': 'Осмотр уха'},
    {'name': 'Владимир Кузнецов', 'direction': 'Терапевт', 'procedure': 'Консультация'},
    {'name': 'Елена Васильева', 'direction': 'Хирург', 'procedure': 'Хирургическая процедура'},
    {'name': 'Дмитрий Николаев', 'direction': 'ЛОР', 'procedure': 'Промывание носа'},
    {'name': 'Светлана Михайлова', 'direction': 'Терапевт', 'procedure': 'Рутинный осмотр'},
    {'name': 'Никита Алексеев', 'direction': 'Хирург', 'procedure': 'Операция на колене'},
    {'name': 'Ольга Сергеева', 'direction': 'ЛОР', 'procedure': 'Лечение ангины'},
    {'name': 'Анна Жукова', 'direction': 'Терапевт', 'procedure': 'Вакцинация'}
]

import asyncio


async def producer(queues: dict[asyncio.Queue], patient_info: list[dict]):
    for patient in patient_info:
        await queues[patient["direction"]].put(patient)
        print(
            f"Регистратор добавил в очередь: {patient['name']}, направление: {patient['direction']}, процедура: {patient['procedure']}"
        )
        await asyncio.sleep(0.1)


async def consumer(queue: asyncio.Queue, doctor_type:str):
    while True:
        patient = await queue.get()
        print(f"{doctor_type} принял пациента: {patient['name']}, процедура: {patient['procedure']}")
        await asyncio.sleep(0.5)
        queue.task_done()


async def main():
    # Полный список вшит в задачу, вставлять его в поле ответа нет необходимости
    # patient_info = []
    queues = {
        'Терапевт': asyncio.Queue(),
        'Хирург': asyncio.Queue(),
        'ЛОР': asyncio.Queue(),
    }

    tasks = [asyncio.create_task(producer(queues, patient_info))]
    for k in queues.keys():
        tasks.append(asyncio.create_task(consumer(queues[k], k)))
    await asyncio.sleep(0)
    for k in queues.keys():
        await queues[k].join()



asyncio.run(main())
