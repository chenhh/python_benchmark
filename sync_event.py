# -*- coding: UTF-8 -*-
import threading
import time


def thread_first_job(a, event):
    # 執行緒進入等待狀況
    print("Wait…")
    event.wait()

    for _ in range(3):
        a += 1
        print(f"This is the thread {a}")


if __name__ == '__main__':

    a = 0
    # 創建 event
    event = threading.Event()
    threads = [
        threading.Thread(target=thread_first_job, args=(a, event)),
        threading.Thread(target=thread_first_job, args=(a, event))
    ]
    for t in threads:
        t.start()
        time.sleep(1)
        # 喚醒處於等待狀態的執行緒
        print("Wake up the thread…")
        event.set()
    [t.join() for t in threads]
# Wait…
# Wake up the thread…
# This is the thread 1
# This is the thread 2
# This is the thread 3
# Wait…
# This is the thread 1
# This is the thread 2
# This is the thread 3
# Wake up the thread…
