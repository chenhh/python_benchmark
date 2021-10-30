# -*- coding: UTF-8 -*-

import timeit
import sys

# print(timeit.timeit('print("hello world")', number=10000))
print(timeit.timeit('sys.stdout.write("hello world");sys.stdout.flush()', number=10000))

