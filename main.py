import numpy as np

from lu_decomposition import lu_decomposition
from plu_decomposition import plu_decomposition
from cholesky import cholesky_decomposition
from qr_decomposition import qr_decomposition
from solve_system import solve
from least_squares import least_squares
from eigenvalues import power_method
from svd import svd
from condition_number import condition_number

def input_matrix():
    rows = int(input("Enter the number of rows for matrix A:"))
    cols = int(input("Enter number of columns for matrix A:"))

    print("\nEnter matrix values row by row (with space seperating entries):")

    matrix = []

    for i in range(rows):
        row = list(map(float, input(f"Row {i + 1}: ").split()))
        matrix.append(row)

    return np.array(matrix)

def input_vector():

    print("\nEnter vector b (with space seperating entries):")
    b = np.array(list(map(float, input().split())))

    return b

def menu():
    print("\nChoose an operation:")
    print("1 - LU Decomposition")
    print("2 - PLU Decomposition")
    print("3 - QR Decomposition")
    print("4 - Cholesky Decomposition")
    print("5 - Solve System (Ax = b)")
    print("6 - Least Squares")
    print("7 - Eigenvalue (Power Method)")
    print("8 - Singular Value Decomposition (SVD)")
    print("9 - Condition Number")
    print("10 - Enter Matrix A")
    print("0 - Exit")

    return int(input("Enter your choice: "))

def pause():
    input("Press ENTER to return to menu.")

def main():
    print("Numerical Linear Algebra Toolkit\n")

    A = input_matrix()

    while True:
        
        choice = menu()

        if choice == 1:
            L, U = lu_decomposition(A)

            print("\nMatrix A:")
            print(A)

            print("\nL matrix:")
            print(L)

            print("\nU matrix:")
            print(U)

            print("\nCheck that A = LU:")
            print(np.dot(L, U)) 

            pause()
        
        elif choice == 2:
            P, L, U = plu_decomposition(A)

            print("\nPermutation Matrix P:")
            print(P)

            print("\nL matrix:")
            print(L)

            print("\nU matrix:")
            print(U)

            print("\nCheck that PA = LU:")
            print(np.dot(P, A))
            print(np.dot(L, U))

            pause()

        elif choice == 3:
            Q, R = qr_decomposition(A)

            print("\nMatrix A:")
            print(A)

            print("\nQ matrix:")
            print(Q)

            print("\nR matrix:")
            print(R)

            print("\nCheck that A = QR:")
            print(np.dot(Q, R))

            pause()

        elif choice == 4:
            L = cholesky_decomposition(A)

            print("\nMatrix A:")
            print(A)

            print("\nL matrix:")
            print(L)

            print("\nCheck LL^T:")
            print(L @ L.T)

            pause()

        elif choice == 5:
            b = input_vector()

            x = solve(A, b)

            print("\nSolution x:")
            print(x)

            print("\nCheck Ax:")
            print(np.dot(A, x))

            pause()

        elif choice == 6:
            b = input_vector()

            x = least_squares(A, b)

            print("\nLeast Squares Solutions:")
            print(x)

            print("\nCheck Ax:")
            print(np.dot(A, x))

            pause()

        elif choice == 7:
            eigenvalue, eigenvector = power_method(A)

            print("\nMatrix A:")
            print(A)

            print("\nDominant EigenValue:")
            print(eigenvalue)

            print("\nEigenvector:")
            print(eigenvector)

            print("\nCheck Ax:")
            print(np.dot(A, eigenvector))

            print("\nlambda x:")
            print(eigenvalue * eigenvector)

            pause()

        elif choice == 8:
            U, S, VT = svd(A)

            print("\nMatrix A:")
            print(A)

            print("\nU matrix:")
            print(U)

            print("\nSigma matrix:")
            print(S)

            print("\nV^T matrix:")
            print(VT)

            print("\nCheck USV^T:")
            print(U @ S @ VT)

            pause()

        elif choice == 9:
            kappa = condition_number(A)

            print("\nMatrix A:")
            print(A)

            print("\nCondition Number:")
            print(kappa)

            pause()

        elif choice == 10:

            print("\nEnter a new matrix A:")
            A = input_matrix()

            pause()

        elif choice == 0:

            print("Exiting Program.")
            break

        else:

            print("\nInvalid choice. Try again.")

if __name__ == "__main__":
    main()