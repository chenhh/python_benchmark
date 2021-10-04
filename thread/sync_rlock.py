# -*- coding: UTF-8 -*-
import threading
import time


class Box(object):
    lock = threading.RLock()

    def __init__(self):
        self.total_items = 0

    def execute(self, n):
        Box.lock.acquire()
        self.total_items += n
        Box.lock.release()

    def add(self):
        Box.lock.acquire()
        self.execute(1)
        Box.lock.release()

    def remove(self):
        Box.lock.acquire()
        self.execute(-1)
        Box.lock.release()


## These two functions run n in separate
## threads and call the Box's methods
def adder(box, items):
    while items > 0:
        print("adding 1 item in the box")
        box.add()
        time.sleep(1)
        items -= 1


def remover(box, items):
    while items > 0:
        print("removing 1 item in the box")
        box.remove()
        time.sleep(1)
        items -= 1


## the main program build some
## threads and make sure it works
if __name__ == "__main__":
    items = 5
    n_thread = 2
    print(f"putting {items} items in the box ")
    box = Box()
    threads = []
    for idx in range(n_thread):
        if idx % 2 == 0:
            threads.append(threading.Thread(target=adder, args=(box, items)))
        else:
            threads.append(threading.Thread(target=remover, args=(box, items)))

    [t.start() for t in threads]
    [t.join() for t in threads]
    print(f"{box.total_items} items still remain in the box ")
