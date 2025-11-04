"""
Поход в подземелье 2.0
"""
import asyncio

players = {
    'DragonSlayer': 0.2,
    'ShadowHunter': 0.6,
    'MagicWizard': 0.8,
    'ElfArcher': 2.0,
    'DarkMage': 1.4,
    'SteelWarrior': 1.6,
    'ThunderBolt': 3.0}


async def enter_dungeon(player: str, time_wait: float, barrier: asyncio.Barrier):
    await asyncio.sleep(time_wait)
    print(f"{player} готов войти в подземелье")
    try:
        await barrier.wait()
        print(f"{player} вошел в подземелье")
    except (asyncio.CancelledError, asyncio.BrokenBarrierError):
        print(f"{player} не смог попасть в подземелье. Группа не собрана")


async def main():
    barrier = asyncio.Barrier(5)
    tasks = [asyncio.create_task(enter_dungeon(p, t, barrier)) for p, t in players.items()]

    await asyncio.wait(tasks, timeout=5)
    await barrier.reset()


asyncio.run(main())
