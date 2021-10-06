# -*- coding: UTF-8 -*-
import multiprocessing as mp


def worker(dictionary, key, item):
    dictionary[key] = item
    print(f"key = {key} value = {item}")


if __name__ == '__main__':
    mgr = mp.Manager()
    dictionary = mgr.dict()
    jobs = [mp.Process(target=worker, args=(dictionary, i, i * 2)) for i in range(10)]
    [j.start() for j in jobs]
    [j.join() for j in jobs]
    print(f'Results: {dictionary}')
