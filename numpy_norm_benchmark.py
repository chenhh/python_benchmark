# -*- coding: utf-8 -*-
import numpy as np
import time
n = 20000
A = np.random.randn(n,n).astype('float64')
B = np.random.randn(n,n).astype('float64')
start_time = time.time()
nrm = np.linalg.norm(A@B)
cost = time.time() - start_time
print(f" took {cost:.3f} seconds ")
print(f" norm = {nrm}")
print(np.__config__.show())


"""
eva00: i7 2600, 16G RAM
Ubuntu 20.04.1, python 3.8, openblas
took 302.797 seconds

eva01: xeon E5-2630v4*2, 32G RAM
the same software environment
took 62.332 seconds

t480s: i5-8250U, 24G RAM
Win10, python 3,8.5, openblas
took: 135.633 seconds

google-cloud
n2d amd-epyc 7B12 8-cores, 32G RAM
Ubuntu 20.04, python 3.8, openblas
took: 179.881 seconds

n2 intel 8-cores, 32G RAM
the same environment,
took 64.369 seconds
"""
