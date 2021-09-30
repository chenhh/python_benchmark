# -*- coding: UTF-8 -*-
import threading


def thread_first_job(t_amount, t_lock):
    # 因為傳入的t_amount是thread間共用的變數
    # 所以寫入時必須先鎖定，否定會有race condition
    for _ in range(10):
        t_lock.acquire()
        t_amount += 1
        print("This is the first thread ", t_amount)
        t_lock.release()


def thread_second_job(t_amount, t_lock):
    for _ in range(10):
        t_lock.acquire()
        t_amount -= 1
        print("This is the second thread ", t_amount)
        t_lock.release()


if __name__ == '__main__':
    amount = 0
    lock = threading.Lock()
    t1 = threading.Thread(target=thread_first_job, args=(amount, lock))
    t2 = threading.Thread(target=thread_second_job, args=(amount, lock))
    threads = (t1, t2)
    [t.start() for t in threads]
    [t.join() for t in threads]
