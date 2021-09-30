# -*- coding: UTF-8 -*-
import threading
from queue import Queue


# 將要傳回的值存入 Queue
def thread_job(data, q):
    for i in range(len(data)):
        data[i] = data[i] * 2
    q.put(data)


def multi_thread():
    data = [[1, 2, 3], [4, 5, 6]]
    q = Queue()
    all_thread = []

    # 使用 multi-thread
    for idx in range(len(data)):
        thread = threading.Thread(target=thread_job, args=(data[idx], q))
        thread.start()
        all_thread.append(thread)

    # 等待全部 Thread 執行完畢
    [t.join() for t in all_thread]

    # 使用 q.get() 取出要傳回的值
    result = [q.get() for _ in range(len(all_thread))]
    print(result)


if __name__ == '__main__':
    multi_thread()
    # [[2, 4, 6], [8, 10, 12]]