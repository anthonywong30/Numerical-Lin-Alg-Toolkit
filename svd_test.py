import numpy as np
from svd import svd

A = np.array([
    [3, 1],
    [1, 3]
])

U, S, VT = svd(A)

print("Matrix A:")
print(A)

print("\nU matrix:")
print(U)

print("\nSigma matrix:")
print(S)

print("\nV^T matrix:")
print(VT)

print("\nCheck USV^T:")
print(U @ S @ VT)

# Output:
# Matrix A:
# [[...]
#  [...]]

# U matrix:
# [[...]
#  [...]]

# Sigma matrix:
# [[...]
#  [...]]

# V^T matrix:
# [[...]
#  [...]]

# Check USV^T:
# [[...]
#  [...]]