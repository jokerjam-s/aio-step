"""
Магическое испытание в Академии Волшебников.
"""
import asyncio
from asyncio import gather

# Словарь заклинаний со временем каста
# Полный словарь заклинаний вшит в задачу
spells = {
    "Огненный шар": 3,
    "Ледяная стрела": 2,
    "Щит молний": 4,
    "Телепортация": 7,
}

# Максимальное время для каста заклинания
max_cast_time = 5  # Секунды

# Ученики мага
students = ["Алара", "Бренн", "Сирил", "Дариа", "Элвин"]


async def cast_spell(student, spell, cast_time):
    await asyncio.sleep(cast_time)
    if cast_time <= max_cast_time:
        print(f"{student} успешно кастует {spell} за {cast_time} сек.")
    else:
        print(
            f"Ученик {student} не справился с заклинанием {spell}, и учитель применил щит. {student} успешно завершает заклинание с помощью shield.")


async def main():
    tasks = []
    for student in students:
        for k, v in spells.items():
            tasks.append(asyncio.create_task(cast_spell(student, k, v)))

    for task in tasks:
        try:
            await asyncio.wait_for(asyncio.shield(task), max_cast_time)
        except TimeoutError:
            await task


asyncio.run(main())
