import numpy as np
from qr_decomposition import qr_decomposition
from backward_sub import backward_sub

def least_squares(A, b):

    Q, R = qr_decomposition(A)

    Qt_b = np.dot(Q.T, b)

    x = backward_sub(R, Qt_b)

    return x