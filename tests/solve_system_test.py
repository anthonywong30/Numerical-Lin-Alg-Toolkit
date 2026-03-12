import numpy as np
from solve_system import solve

A = np.array([
    [2, 3, 1],
    [4, 7, 7],
    [6, 18, 22]
])

b = np.array([1, 2, 3])
x = solve(A, b)

print("Solution x:")
print(x)

print("\nCheck Ax:")
print(np.dot(A, x))

# Output:
# Solution x:
# [0.5. 0. 0.]

# Check Ax:
# [1. 2. 3.]