# -*- coding: UTF-8 -*-
import _thread
import threading
import time

exitFlag = 0


class MyThread(threading.Thread):
    def __init__(self, thread_id, name, counter):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.counter = counter

    def run(self):
        print(f"{self.thread_id} starting: {self.name}")
        print_time(self.name, self.counter, 2)
        print(f"{self.thread_id} exiting {self.name}")


def print_time(thread_name, delay, counter):
    while counter:
        if exitFlag:
            # Python3中已經不能使用thread，以_thread取代
            _thread.exit()
        time.sleep(delay)
        print(f"{thread_name} {time.ctime(time.time())}")
        counter -= 1


if __name__ == '__main__':
    # Create new threads
    threads = (MyThread(1, "Thread-1", 1), MyThread(2, "Thread-2", 2))

    # Start new Threads
    [t.start() for t in threads]

    # wait child threads complete
    [t.join() for t in threads]
    print("Exiting Main Thread")
