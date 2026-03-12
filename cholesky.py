import numpy as np

def cholesky_decomposition(A):

    n = A.shape[0]
    L = np.zeros((n, n))

    for i in range(n):
        for j in range(i + 1):

            if i == j:
                sum_val = sum(L[i][k] ** 2 for k in range(j))
                L[i][j] = np.sqrt(A[i][i] - sum_val)

            else:
                sum_val = sum(L[i][k] * L[j][k] for k in range(j))
                L[i][j] = (A[i][j] - sum_val) / L[j][j]

    return L