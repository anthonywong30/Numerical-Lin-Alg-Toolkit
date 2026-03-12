import numpy as np
from plu_decomposition import plu_decomposition

A = np.array([
    [2, 3, 1],
    [4, 7, 7],
    [6, 18, 22]
])

P, L, U = plu_decomposition(A)

print("Permutation Matrix P:")
print(P)

print("\nL matrix:")
print(L)

print("\nU matrix:")
print(U)

print("\nCheck that PA = LU:")
print(np.dot(P, A))
print(np.dot(L, U))

# Output:
# PA matrix:
# [[6. 18. 22.]
#  [4. 7. 7.]
#  [2. 3. 1.]]

# LU matrix:
# [[6. 18. 22.]
#  [4. 7. 7.]
#  [2. 3. 1.]]