# -*- coding: utf-8 -*-
import numpy as np
import time
n = 20000
A = np.random.randn(n,n).astype('float64')
B = np.random.randn(n,n).astype('float64')
start_time = time.time()
nrm = np.linalg.norm(A@B)
print(" took {} seconds ".format(time.time() - start_time))
print(" norm = ",nrm)
print(np.__config__.show())


"""
eva00: Ubuntu 20.04.1, python 3.8, openblas
took 302.79740262031555 seconds

eva01: the same environment
took 62.331828594207764 seconds
"""
