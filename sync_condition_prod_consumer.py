# -*- coding: UTF-8 -*-
from threading import (Thread, Condition)
import time


class Consumer(Thread):
    """ 消費者 """
    def __init__(self, _items, _condition):
        super().__init__()
        self.items = _items
        self.condition = _condition

    def consume(self):
        # 要求lock
        self.condition.acquire()
        if len(self.items) == 0:
            self.condition.wait()
            print("消費者: 沒有產品了")
        self.items.pop()
        print(f"消費者: 使用1個產品，還有{len(self.items)}個產品")
        # 喚醒等待的執行緒
        self.condition.notify()
        # 釋放lock
        self.condition.release()

    def run(self):
        for _ in range(0, 20):
            time.sleep(1)
            self.consume()


class Producer(Thread):
    """ 生產者 """
    def __init__(self, _items, _condition):
        super().__init__()
        self.items = _items
        self.condition = _condition

    def produce(self):
        self.condition.acquire()
        if len(self.items) == 10:
            self.condition.wait()
            print(f"生產者:現在產品滿了，有{len(self.items)}個產品，停止生產")
        self.items.append(1)
        print(f"生產者:生產1個，現在共有{len(self.items)}個產品")
        self.condition.notify()
        self.condition.release()

    def run(self):
        for i in range(0, 20):
            time.sleep(0.5)
            self.produce()


if __name__ == "__main__":
    items = []
    condition = Condition()

    producers = (Producer(items, condition), Producer(items, condition), Producer(items, condition))
    consumers = (Consumer(items, condition), Consumer(items, condition), Consumer(items, condition))
    [p.start() for p in producers]
    [c.start() for c in consumers]
    [p.join() for p in producers]
    [c.join() for c in consumers]

