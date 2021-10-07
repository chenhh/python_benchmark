# -*- coding: UTF-8 -*-
import asyncio
import time


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main():
    task1 = asyncio.create_task(
        say_after(1, 'hello'))

    task2 = asyncio.create_task(
        say_after(2, 'world'))

    print(f"started at {time.strftime('%X')}")

    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")

if __name__ == '__main__':
    # 在main內使用create_tasks平行處理
    # 所以只花了2秒就執行完成
    asyncio.run(main())
    """
    started at 17:54:53
    hello
    world
    finished at 17:54:55
    """