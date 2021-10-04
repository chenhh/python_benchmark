# -*- coding: UTF-8 -*-

import threading


def thread_first_job(t_a, sem):
    for _ in range(10):
        # 取得旗標
        sem.acquire()
        t_a += 1
        print(f"This is the first thread {t_a}")
        # 釋放旗標
        sem.release()


def thread_second_job(t_a, sem):
    for _ in range(10):
        # 取得旗標
        sem.acquire()
        t_a -= 1
        print(f"This is the second thread {t_a}")
        # 釋放旗標
        sem.release()


if __name__ == '__main__':
    a = 0
    # 設定旗標計數器為2
    semaphore = threading.Semaphore(2)
    t_1 = threading.Thread(target=thread_first_job, args=(a, semaphore))
    t_2 = threading.Thread(target=thread_second_job, args=(a, semaphore))
    threads = (t_1, t_2)
    [t.start() for t in threads]
    [t.join() for t in threads]
