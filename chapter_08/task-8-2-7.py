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


async def producer(queues: dict[asyncio.Queue], patient_info: dict):
    await queues[patient_info["direction"]].put(patient_info)
    print(
        f"Регистратор добавил в очередь: {patient_info['name']}, направление: {patient_info['direction']}, процедура: {patient_info['procedure']}"
    )


async def consumer(queue, doctor_type):
    pass


async def main():
    # Полный список вшит в задачу, вставлять его в поле ответа нет необходимости
    # patient_info = []
    queues = {
        'Терапевт': asyncio.Queue(),
        'Хирург': asyncio.Queue(),
        'ЛОР': asyncio.Queue(),
    }

    pass


asyncio.run(main())
