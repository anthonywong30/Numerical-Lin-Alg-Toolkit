import numpy as np

def power_method(A, max_iter = 1000, tol = 1e-10):

    n = A.shape[0]

    x = np.random.rand(n)

    #normalize x
    x = x / np.linalg.norm(x)

    eigenvalue = 0

    for _ in range(max_iter):
        
        y = np.dot(A, x)

        new_eigenvalue = np.dot(x, y)

        x = y / np.linalg.norm(y)

        if abs(new_eigenvalue - eigenvalue) < tol:
            break

        eigenvalue = new_eigenvalue
    
    return eigenvalue, x