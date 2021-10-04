# -*- coding: UTF-8 -*-
import threading
import time


def thread_first_job(x):
    name = threading.currentThread().getName()
    time.sleep(5)
    print(f"thread name:{name}, 1st job: {x}")
    print(f"thread name:{name}, 1st job finished")


def thread_second_job(x):
    name = threading.currentThread().getName()
    print(f"thread name:{name}, 2nd job: {x}")
    print(f"thread name:{name}, 2nd job finished")


if __name__ == '__main__':
    t1 = threading.Thread(target=thread_first_job, args=("Hi",))
    t2 = threading.Thread(target=thread_second_job, args=("Hello",))
    # t2的daemon設為true, 則不論t1是否結束, t2會和main thread一起結束,
    # 必須寫在t2.start之前
    t2.setDaemon(True)
    t1.start()
    t2.start()
    print("main thread finished")

    """
    thread name:Thread-2, 2nd job: Hello
    thread name:Thread-2, 2nd job finished
    main thread finished
    thread name:Thread-1, 1st job: Hi
    thread name:Thread-1, 1st job finished
    """
