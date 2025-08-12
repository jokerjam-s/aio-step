"""
Прогноз погоды.
"""
import asyncio
import random

# Не менять!
random.seed(0)

async def fetch_weather(source, city):
    await asyncio.sleep(random.randint(1,5))
    temperature = random.randint(-10, 35)
    return f"Данные о погоде получены из источника {source} для города {city}: {temperature}°C"

async def main():
    city = "Москва"
    sources = [
        'http://api.weatherapi.com',
        'http://api.openweathermap.org',
        'http://api.weatherstack.com',
        'http://api.weatherbit.io',
        'http://api.meteostat.net',
        'http://api.climacell.co'
    ]

    tasks = [asyncio.create_task(fetch_weather(s, city)) for s in sources]
    await asyncio.sleep(.5)

    while True:
        if any([t.done() for t in tasks]):
            _ = [t.cancel() for t in tasks]
            break
        await asyncio.sleep(0.5)

    # done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    # for task in pending:
    #     task.cancel()


asyncio.run(main())