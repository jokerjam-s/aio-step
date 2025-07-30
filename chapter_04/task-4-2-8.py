"""
Напишите асинхронный код, который имитирует обработку логов событий сервера.
Каждое событие имеет свою уникальную задержку обработки (на ответ сервера).
"""
import asyncio

# Пример данных
log_events = [
    {"event": "Запрос на вход", "delay": 0.5},
    {"event": "Запрос данных пользователя", "delay": 1.0},
    {"event": "Обновление данных пользователя", "delay": 1.5},
    {"event": "Обновление конфигурации сервера", "delay": 5.0},
]


async def fetch_log(event: dict):
    await asyncio.sleep(event["delay"])
    return f"Событие: '{event["event"]}' обработано с задержкой {event["delay"]} сек."


async def main():
    tasks = [asyncio.create_task(fetch_log(e)) for e in log_events]
    results = await asyncio.gather(*tasks)

    for result in results:
        print(result)


if __name__ == "__main__":
    asyncio.run(main())
