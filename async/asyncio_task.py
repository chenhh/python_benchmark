# -*- coding: UTF-8 -*-
import asyncio
import time

async def do_some_work(x):
    print(f'Waiting: {x}')
    await asyncio.sleep(x)
    return f'Done after {x}s'


if __name__ == '__main__':
    now = lambda: time.time()
    start = now()
    coroutine1 = do_some_work(1)
    coroutine2 = do_some_work(2)
    coroutine3 = do_some_work(4)

    tasks = [
        asyncio.ensure_future(coroutine1),
        asyncio.ensure_future(coroutine2),
        asyncio.ensure_future(coroutine3)
    ]

    loop = asyncio.get_event_loop()
    # loop.run_until_complete(asyncio.wait(tasks))
    loop.run_until_complete(asyncio.gather(*tasks))

    for task in tasks:
        print(f'Task ret: {task.result()}')

    print(f'TIME: {now() - start}')
