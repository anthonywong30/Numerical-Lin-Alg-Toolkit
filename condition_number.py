import numpy as np

def condition_number(A):

    A_inv = np.linalg.inv(A)

    norm_A = np.linalg.norm(A, 2)
    norm_A_inv = np.linalg.norm(A_inv, 2)

    kappa = norm_A * norm_A_inv

    return kappa