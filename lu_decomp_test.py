import numpy as np
from lu_decomposition import lu_decomposition

#from lu_decomposition import lu_decomposition

A = np.array([
    [2, 3, 1],
    [4, 7, 7],
    [6, 18, 22]
])

L, U = lu_decomposition(A)

print("Matrix A:")
print(A)

print("\nL matrix:")
print(L)

print("\nU matrix:")
print(U)

print("\nCheck that A = LU:")
print(np.dot(L, U))

# Output:
# Matrix A:
# [[2 3 1]
#  [4 7 7]
#  [6 18 22]]

# L matrix:
# [[1. 0. 0.]
#  [2. 1. 0.]
#  [3. 0. 1.]]

# U matrix:
# [[2 3 1]
#  [0. 1. 5.]
#  [0. 0. -26.]]

# Check that A = LU:
# [[2 3 1]
#  [4 7 7]
#  [6 18 22]]