import asyncio


# объявление асинхронной функции producer, принимающей аргумент queue
async def producer(queue, prod_range):
    for i in range(*prod_range):
        item = f'Элемент {i}'  # создание строки с элементом и его номером
        await queue.put(item)  # добавление элемента в очередь
        print(f'{asyncio.current_task().get_name()} добавил в очередь элемент: {item}')
        # переключение контекста, позволяющее работать задачам асинхронно
        await asyncio.sleep(0)


# объявление асинхронной функции consumer, принимающей аргумент queue
async def consumer(queue):
    while True:
        item = await queue.get()  # получение элемента из очереди
        print(f'{asyncio.current_task().get_name()} получил из очереди элемент: {item}')
        # указание, что ранее поставленная в очередь задача завершена
        queue.task_done()
        # переключение контекста, позволяющее работать задачам асинхронно
        await asyncio.sleep(0)


async def main():
    queue = asyncio.Queue()  # создание очереди

    # создание задач для функции producer и consumer
    prod_task_1 = asyncio.create_task(producer(queue, (0, 10, 2)), name='Производитель_1')
    prod_task_2 = asyncio.create_task(producer(queue, (1, 10, 2)), name='Производитель_2')
    cons_task = asyncio.create_task(consumer(queue), name='Потребитель')
    # Список имен незавершенных задач
    print([task.get_name() for task in
           asyncio.all_tasks()])  # ['Task-1', 'Производитель_1', 'Производитель_2', 'Потребитель']
    # Запуск созданных задач на await (переключение контекста)
    await asyncio.sleep(0)

    # Выполнение Task-1 блокируется до "истощения" очереди
    await queue.join()
    print([task.get_name() for task in asyncio.all_tasks()])  # ['Task-1', 'Потребитель']
    # Отмена cons_task ('Потребитель'), из-за бесконечного цикла она не завершится сама.
    cons_task.cancel()
    await asyncio.sleep(0)  # Переключение контекста для выполнения запроса на отмену задачи
    print([task.get_name() for task in asyncio.all_tasks()])  # ['Task-1']


asyncio.run(main())
