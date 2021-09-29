# -*- coding: UTF-8 -*-
import threading
import time


def first_function():
    t_name = threading.currentThread().getName()
    print(f"{t_name} is starting")
    time.sleep(2)
    #
    print(f"{t_name} is exiting")
    return


def second_function():
    t_name = threading.currentThread().getName()
    print(f"{t_name} is starting")
    time.sleep(2)
    print(f"{t_name} is exiting")
    return


def third_function():
    t_name = threading.currentThread().getName()
    print(f"{t_name} is starting")
    time.sleep(2)
    print(f"{t_name} is exiting")
    return


if __name__ == "__main__":
    # 建立Thread object
    # target 是用於 run() 方法調用的可調用對象。
    t1 = threading.Thread(name='1st_thread',
                          target=first_function)
    t2 = threading.Thread(name='2nd_thread',
                          target=second_function)
    t3 = threading.Thread(name='3rd_thread',
                          target=third_function)
    # start thread
    # 建立thread時, 因為t1, t2, t3是依序建立,
    # 所以在印出starting時不會亂序
    t1.start()
    t2.start()
    t3.start()
    # wait thread finish
    # thread完成時，不一定會按照次序，所以exiting會亂序
    t1.join()
    t2.join()
    t3.join()
    print("finished")

# 1st_thread is starting
# 2nd_thread is starting
# 3rd_thread is starting
# 2nd_thread is exiting
# 1st_thread is exiting
# 3rd_thread is exiting