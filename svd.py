import numpy as np

def svd(A):

    A = A.astype(float)

    ATA = np.dot(A.T, A)

    eigenvalues, V = np.linalg.eig(ATA)

    singular_values = np.sqrt(np.abs(eigenvalues))

    idx = np.argsort(-singular_values)

    singular_values = singular_values[idx]
    V = V[:, idx]

    U = np.dot(A, V)

    for i in range(len(singular_values)):
        if singular_values[i] > 1e-10:
            U[:, i] = U[:, i] / singular_values[i]

    m, n = A.shape
    Sigma = np.zeros((m,n))

    for i in range(min(m, n)):
        Sigma[i, i] = singular_values[i]

    return U, Sigma, V.T