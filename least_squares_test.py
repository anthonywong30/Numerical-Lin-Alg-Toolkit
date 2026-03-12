import numpy as np
from least_squares import least_squares

A = np.array([
    [1, 1],
    [1, 2],
    [1, 3]
])

b = np.array([1, 2, 2])
x = least_squares(A, b)

print("Least Squares Solutions:")
print(x)

print("\nCheck Ax:")
print(np.dot(A, x))

#Output:
# Least Squares Solutions:
# [0.67 0.5]

# Check Ax:
# [1.167 1.667 2.167]