"""
Инвентаризация библиотеки
"""
import asyncio

books_json = [
    {
        "Порядковый номер": 1,
        "Автор": "Rebecca Butler",
        "Название": "Three point south wear score organization.",
        "Год издания": "1985",
        "Наличие на полке": True
    },
    {
        "Порядковый номер": 2,
        "Автор": "Mark Cole",
        "Название": "Drive experience customer somebody pressure.",
        "Год издания": "1985",
        "Наличие на полке": False
    },
]


async def check_book(book: dict) -> str | None:
    await asyncio.sleep(.1)
    if not book["Наличие на полке"]:
        return f"{book["Порядковый номер"]}: {book["Автор"]}: {book["Название"]} ({book["Год издания"]})"
    raise RuntimeError("Книга на полке.")


async def main():
    tasks = [check_book(b) for b in books_json]
    results = await asyncio.gather(*tasks, return_exceptions=True)

    for result in results:
        if not isinstance(result, Exception):
            print(result)


asyncio.run(main())
