import asyncio

news_list = [
    "Новая волна COVID-19 обрушилась на Европу",
    "Рынки акций растут на фоне новостей о вакцине",
]


async def analyze_news(keyword: str, news_list: list[str], delay: float):
    for news in news_list:
        if news.count(keyword):
            print(f"Найдено соответствие для '{keyword}': {news}")
            await asyncio.sleep(delay)


async def main():
    # Создаем асинхронные задачи для каждой корутины с разными ключевыми словами и задержками
    task1 = asyncio.create_task(analyze_news('COVID-19', news_list, 0.2))
    task2 = asyncio.create_task(analyze_news('игр', news_list, 0.2))
    task3 = asyncio.create_task(analyze_news('новый вид', news_list, 0.2))

    # Ожидаем выполнения всех задач
    await asyncio.gather(task1, task2, task3)


asyncio.run(main())
