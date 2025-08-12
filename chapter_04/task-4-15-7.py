"""
Веб приложение с поддержкой нескольких языков.
"""
import asyncio
import contextvars

# Контекстная переменная для хранения текущего языка
current_language = contextvars.ContextVar("current_language")


def set_language(language_code):
    current_language.set(language_code)


async def get_greeting():
    greetings = {
        'en': "Hello!",
        'ru': "Привет!",
        'es': "Hola!"
    }
    return greetings.get(current_language.get())


async def get_error_message():
    error_messages = {
        'en': "An error occurred.",
        'ru': "Произошла ошибка.",
        'es': "Ocurrió un error."
    }
    return error_messages.get(current_language.get())


async def test_user_actions(language_code):
    current_language.set(language_code)
    print(await get_greeting())
    print(await get_error_message())


async def main():
    await asyncio.gather(
        test_user_actions("en"),
        test_user_actions("ru"),
        test_user_actions("es")
    )


asyncio.run(main())
