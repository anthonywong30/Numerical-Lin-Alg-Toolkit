import numpy as np
from condition_number import condition_number

A = np.array([
    [1, 2],
    [2, 4.0001]
])

kappa = condition_number(A)

print("Matrix A:")
print(A)

print("\nCondition Number:")
print(kappa)

# Output:
# Matrix A:
# [[1. 2.]
#  [2. 4.001]]

# Condition Number: