# -*- coding: UTF-8 -*-
import asyncio
import time


async def say_after(delay: int, what: str):
    await asyncio.sleep(delay)
    print(what)


async def main():
    print(f"started at {time.strftime('%X')}")

    await say_after(1, 'hello')
    await say_after(2, 'world')

    print(f"finished at {time.strftime('%X')}")


if __name__ == '__main__':
    # sequential execute multiple coroutines
    asyncio.run(main())
    """
    started at 17:45:50
    hello
    world
    finished at 17:45:53
    """