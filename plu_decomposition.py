import numpy as np

def plu_decomposition(A):

    n = len(A)

    P = np.eye(n)
    L = np.zeros((n, n))
    U = A.astype(float).copy()

    for k in range(n):
        pivot = np.argmax(abs(U[k:, k])) + k

        if pivot != k:
            U[[k, pivot]] = U[[pivot, k]]
            P[[k, pivot]] = P[[pivot, k]]
            L[[k, pivot], :k] = L[[pivot, k], :k]

        for i in range(k + 1, n):

            factor = U[i][k] / U[k][k]
            L[i][k] = factor
            U[i] = U[i] - factor * U[k]

    np.fill_diagonal(L, 1)

    return P, L, U