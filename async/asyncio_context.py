# -*- coding: UTF-8 -*-
import asyncio


async def compute(x, y):
    print(f"Compute {x} + {y} ...")
    await asyncio.sleep(1.0)
    return x + y


async def print_sum(x, y):
    result = await compute(x, y)
    print(f"{x} + {y} = {result}")


if __name__ == '__main__':
    asyncio.run(print_sum(1, 2))
