"""
Запуск корутин вручную.
"""
import asyncio

async def main():
    print("Корутина завершена")

loop = asyncio.new_event_loop()
loop.run_until_complete(main())
loop.close()