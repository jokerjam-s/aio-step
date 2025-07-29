import asyncio

# Полный словарь students вшит в задачу, вставлять его не нужно
students = {
    "Алекс": {"course": "Асинхронный Python", "steps": 515, "speed": 78},
    "Мария": {"course": "Многопоточный Python", "steps": 431, "speed": 62},
    "Иван": {"course": "WEB Парсинг на Python", "steps": 491, "speed": 57}
}


async def study_course(student, course, steps, speed):
    print(f"{student} начал проходить курс {course}.")
    tm = round(steps / speed, 2)
    await asyncio.sleep(tm)
    print(f"{student} прошел курс {course} за {tm} ч.")


async def main():
    # Создание задач с помощью asyncio.create_task для каждого студента
    tasks = [asyncio.create_task(study_course(k, v['course'], v['steps'], v['speed'])) for k, v in students.items()]

    # Ожидание завершения каждой задачи индивидуально
    await asyncio.gather(*tasks)


asyncio.run(main())
