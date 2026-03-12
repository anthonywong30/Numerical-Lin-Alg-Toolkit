import numpy as np

def lu_decomposition(A):

    n = len(A)

    L = np.eye(n)
    U = A.astype(float).copy()

    for k in range(n - 1):
        for i in range(k + 1, n):
            factor = U[i][k] / U[k][k]
            L[i][k] = factor
            U[i] = U[i] - factor * U[k]

    return L, U