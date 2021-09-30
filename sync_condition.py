# -*- coding: UTF-8 -*-
import threading


def thread_first_job(a, cond):
    # 取得 lock
    cond.acquire()
    print("Acquire the condition lock")
    # 執行緒進入等待狀況
    if a == 0:
        print("Wait…")
        cond.wait()
    # 喚醒執行緒
    print("Notify to wake up…")
    cond.notify()

    for _ in range(3):
        a += 1
        print("This is the first thread ", a)

    # 釋放 lock
    cond.release()


def thread_second_job(a, cond):
    # 取得 lock
    cond.acquire()

    # 喚醒執行緒
    cond.notify()
    a += 1

    # 釋放 lock
    cond.release()


if __name__ == '__main__':
    a = 0
    cond = threading.Condition()
    threads = [
        threading.Thread(target=thread_first_job, args=(a, cond)),
        threading.Thread(target=thread_second_job, args=(a, cond))]
    [t.start() for t in threads]
    [t.join() for t in threads]
# Acquire the condition lock
# Wait…
# Notify to wake up…
# This is the first thread  1
# This is the first thread  2
# This is the first thread  3