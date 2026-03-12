import numpy as np
from qr_decomposition import qr_decomposition

A = np.array([
    [1, 1],
    [1, 0],
    [0, 1]
])

Q, R = qr_decomposition(A)

print("Matrix A:")
print(A)

print("\nQ matrix:")
print(Q)

print("\nR matrix:")
print(R)

print("\nCheck that A = QR:")
print(np.dot(Q, R))

#Output:
# Matrix A:
# [...]

# Matrix Q:
# [...]

# Matrix R:
# [...]

# Matrix QR:
# [...]

# Where matrix A = matrix QR