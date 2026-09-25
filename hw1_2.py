## This is the file for the second homework question. 
# Write a function (either MATLAB, Python or your preferred language) to perform
# the LU factorization (with row and column pivoting). Your input should be a nonsingular
# n×n matrix A. Your output should be a lower triangular matrix L and an upper triangular
# matrix U such that A = LU . Test your code with different matrices and compare the results
# with those obtained using built-in commands in MATLAB or Python
import numpy as np
import scipy 
A=np.random.rand(8, 8)
print("Original matrix:")
print(A)
def lu_factorization(matrix):
    n = matrix.shape[0]
    L = np.eye(n)
    U = matrix.copy()
    P = np.eye(n)
    
    for i in range(n):
        pivot_row = i + np.argmax(np.abs(U[i:, i]))
        
        if U[pivot_row, i] == 0:
            raise ValueError("Matrix is singular and cannot be decomposed.")
        
        if pivot_row != i:
            U[[i, pivot_row], :] = U[[pivot_row, i], :]
            P[[i, pivot_row], :] = P[[pivot_row, i], :]
            
            if i > 0:
                L[[i, pivot_row], :i] = L[[pivot_row, i], :i]
                
        for j in range(i + 1, n):
            factor = U[j, i] / U[i, i]
            L[j, i] = factor
            U[j, i:] -= factor * U[i, i:]
    print("L matrix:")
    print(L)
    print("U matrix:")
    print(U)
    print("P matrix:")
    print(P)
    print("Verification (P @ L @ U):")
    print(P @ L @ U)
    print("Difference between the original matrix and P @ L @ U:")
    print(A - P @ L @ U)
        
def sanity_check():
    ## This should use built in functions to do what the previous function does.
    L_builtin, U_builtin,P_builtin = scipy.linalg.lu(A)
    print("Built-in L matrix:")
    print(L_builtin)
    print("Built-in U matrix:")
    print(U_builtin)
    print("Built-in P matrix:")
    print(P_builtin)
    print("Verification (Built-in P @ L @ U):")
    print(P_builtin @ L_builtin @ U_builtin)
    print("Difference between the original matrix and Built-in P @ L @ U:")
    print(A - P_builtin @ L_builtin @ U_builtin)


    

lu_factorization(A)
sanity_check()