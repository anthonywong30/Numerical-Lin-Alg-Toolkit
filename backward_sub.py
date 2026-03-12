import numpy as np

def backward_sub(U, y):

    n = len(y)
    x = np.zeros(n)

    for i in reversed(range(n)):
        x[i] = (y[i] - np.dot(U[i, i + 1:], x[i + 1:])) / U[i, i]

    return x