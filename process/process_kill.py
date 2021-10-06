# -*- coding: UTF-8 -*-
"""
我們可以使用 terminate() 方法立即殺死一個行程。
另外，我們可以使用 is_alive() 方法來判斷一個行程是否還存活。
"""
import multiprocessing
import time


def foo():
    print('Starting function')
    time.sleep(0.1)
    print('Finished function')


if __name__ == '__main__':
    p = multiprocessing.Process(target=foo)
    print(f'Process before execution: {p}, {p.is_alive()}')
    p.start()
    print(f'Process running: {p}, {p.is_alive()}')
    p.terminate()
    print(f'Process terminated:  {p}, {p.is_alive()}')
    p.join()
    print(f'Process joined:  {p}, {p.is_alive()}')
    print(f'Process exit code: {p.exitcode}')
    # -15 。負數表示子行程被數字為15的信號殺死。
