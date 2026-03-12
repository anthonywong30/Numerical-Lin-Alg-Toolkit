import numpy as np
from eigenvalues import power_method

A = np.array([
    [4, 1],
    [2, 3]
])

eigenvalue, eigenvector = power_method(A)

print("Matrix A:")
print(A)

print("\nDominant EigenValue:")
print(eigenvalue)

print("\nEigenvector:")
print(eigenvector)

print("\nCheck Ax:")
print(np.dot(A, eigenvector))

print("\nlambda x:")
print(eigenvalue * eigenvector)

# Output:
# Dominant Eigenvalue:
# 5.0

# EigenVector:
# [0.707 0.707]

# Check Ax:
# [...]

# Lambda x:
# [...]