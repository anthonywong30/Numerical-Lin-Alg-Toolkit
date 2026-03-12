import numpy as np
from plu_decomposition import plu_decomposition
from forward_sub import forward_sub
from backward_sub import backward_sub

def solve(A, b):

    P, L, U = plu_decomposition(A)

    Pb = np.dot(P, b)

    y = forward_sub(L, Pb)
    x = backward_sub(U, y)

    return x