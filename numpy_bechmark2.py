# -*- coding: UTF-8 -*-

# Roughly based on: http://stackoverflow.com/questions/11443302/compiling-numpy-with-openblas-integration

from __future__ import print_function

import numpy as np
from time import time

# Let's take the randomness out of random numbers (for reproducibility)
np.random.seed(0)

size = 4096
A, B = np.random.random((size, size)), np.random.random((size, size))
C, D = np.random.random((size * 128,)), np.random.random((size * 128,))
E = np.random.random((int(size / 2), int(size / 4)))
F = np.random.random((int(size / 2), int(size / 2)))
F = np.dot(F, F.T)
G = np.random.random((int(size / 2), int(size / 2)))

# Matrix multiplication
N = 20
t = time()
for i in range(N):
    np.dot(A, B)
delta = time() - t
print('Dotted two %dx%d matrices in %0.2f s.' % (size, size, delta / N))
del A, B

# Vector multiplication
N = 5000
t = time()
for i in range(N):
    np.dot(C, D)
delta = time() - t
print('Dotted two vectors of length %d in %0.2f ms.' % (size * 128, 1e3 * delta / N))
del C, D

# Singular Value Decomposition (SVD)
N = 3
t = time()
for i in range(N):
    np.linalg.svd(E, full_matrices = False)
delta = time() - t
print("SVD of a %dx%d matrix in %0.2f s." % (size / 2, size / 4, delta / N))
del E

# Cholesky Decomposition
N = 3
t = time()
for i in range(N):
    np.linalg.cholesky(F)
delta = time() - t
print("Cholesky decomposition of a %dx%d matrix in %0.2f s." % (size / 2, size / 2, delta / N))

# Eigendecomposition
t = time()
for i in range(N):
    np.linalg.eig(G)
delta = time() - t
print("Eigendecomposition of a %dx%d matrix in %0.2f s." % (size / 2, size / 2, delta / N))

print('')
print('This was obtained using the following Numpy configuration:')
np.__config__.show()

"""
t480s: openblas
Dotted two 4096x4096 matrices in 1.09 s.
Dotted two vectors of length 524288 in 0.26 ms.
SVD of a 2048x1024 matrix in 1.24 s.
Cholesky decomposition of a 2048x2048 matrix in 0.13 s.
Eigendecomposition of a 2048x2048 matrix in 7.61 s.


eva01:
Dotted two 4096x4096 matrices in 0.92 s.
Dotted two vectors of length 524288 in 0.05 ms.
SVD of a 2048x1024 matrix in 1.31 s.
Cholesky decomposition of a 2048x2048 matrix in 0.24 s.
Eigendecomposition of a 2048x2048 matrix in 13.55 s

"""