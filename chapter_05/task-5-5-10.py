"""
Помощь с отчетами.
"""
import asyncio

reports = [
    {"name": "Алексей Иванов", "report": "Отчет о прибылях и убытках", "load_time": 5},
    {"name": "Мария Петрова", "report": "Прогнозирование движения денежных средств", "load_time": 4},
    {"name": "Иван Смирнов", "report": "Оценка инвестиционных рисков", "load_time": 3},
    {"name": "Елена Кузнецова", "report": "Обзор операционных расходов", "load_time": 2},
    {"name": "Дмитрий Орлов", "report": "Анализ доходности активов", "load_time": 10}
]


async def download_data(report):
    try:
        if report["name"] == "Дмитрий Орлов":
            await cancel_task(asyncio.current_task())
    except asyncio.CancelledError:
        print(f"Загрузка отчета {report["report"]} для пользователя {report["name"]} остановлена. Введите новые данные")
    else:
        await asyncio.sleep(report["load_time"])
        print(f"Отчет: {report["report"]} для пользователя {report["name"]} готов")


async def cancel_task(task):
    task.cancel()
    await asyncio.sleep(0)


async def main():
    tasks = [asyncio.create_task(download_data(r)) for r in reports]
    await asyncio.wait(tasks, return_when=asyncio.ALL_COMPLETED)


asyncio.run(main())
