# -*- coding: UTF-8 -*-
import multiprocessing
import time

"""
後台行程不允許創建子行程。否則，當後台行程跟隨父行程退出的時候，子行程會變成孤兒行程。
另外，它們並不是Unix的守護行程或服務（daemons or services），
所以當非後台行程退出，它們會被終結。
"""

def foo():
    name = multiprocessing.current_process().name
    print(f"Starting {name}")
    time.sleep(1)
    print(f"Exiting {name}")


if __name__ == '__main__':
    bg_p = multiprocessing.Process(name='background_process', target=foo)
    # 在非後台運行的行程會看到一個輸出，後台運行的沒有輸出，後台運行行程在主行程結束之後會自動結束。
    bg_p.daemon = True
    fg_p = multiprocessing.Process(name='NO_background_process', target=foo)
    fg_p.daemon = False
    ps = (bg_p, fg_p)
    [p.start() for p in ps]
    [p.join() for p in ps]
    print("main process finished")