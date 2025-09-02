"""
Асинхронные уведомления блогера Васи/
"""
import asyncio


# Объявите корутину publish_post: принимает на вход текст поста и имитирует публикацию нового поста на блоге Васи
async def publish_post(text: str):
    print(f"Пост опубликован: {text}")


# Объявите корутину notifier: принимает имя подписчика и имитирует оповещение о публикации поста.
async def notifier(subscriber):
    print(f"Уведомление отправлено {subscriber}")


# Объявите корутину notify_subscribers: принимает на вход список подписчиков и реализует отправку уведомления каждому подписчику
async def notify_subscribers(subscribers):
    tasks = [asyncio.create_task(notifier(s)) for s in subscribers]
    await asyncio.sleep(0)


async def main():
    post_text = "Hello world!"
    subscribers = ["Alice", "Bob", "Charlie", "Dave", "Emma", "Frank", "Grace", "Henry", "Isabella", "Jack"]
    task1 = asyncio.create_task(publish_post(post_text))
    task2 = asyncio.create_task(notify_subscribers(subscribers))
    await asyncio.gather(task1, task2)

# запускаем асинхронную функцию main()
asyncio.run(main())