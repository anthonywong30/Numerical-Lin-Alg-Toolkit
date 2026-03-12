import numpy as np
from cholesky import cholesky_decomposition

A = np.array([
    [4, 2],
    [2, 3]
])

L = cholesky_decomposition(A)

print("Matrix A:")
print(A)

print("\nL matrix:")
print(L)

print("\nCheck LL^T:")
print(L @ L.T)

# Output:
# Matrix A:
# [[...]
#  [...]]

# L matrix:
# [[...]
#  [...]]

# Check LL^T:
# [[...]
#  [...]]