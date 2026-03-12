import numpy as np

def is_square(A):
    return A.shape[0] == A.shape[1]

def is_symmetric(A, tol = 1e-10):
    return np.allclose(A, A.T, atol = tol)

def vector_norm(x):
    return np.sqrt(np.sum(x**2))

def frobenius_norm(A):
    return np.sqrt(np.sum(A**2))

def is_orthogonal(Q, tol = 1e-10):
    I = np.eye(Q.shape[1])
    return np.allclose(Q.T @ Q, I, atol = tol)

def random_matrix(m, n):
    return np.random.rand(m, n)