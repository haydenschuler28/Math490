## This is the file for homework question 1.
# a. Print out A on your computer screen. Can you tell by looking at it that it has
# (numerical) rank 4? Briefly explain your observation.
## Honestly I can't tell by looking at it that it has rank 4. The decimals aren't intutive enoguh to see clear linear dependence. 
# b. Use MATLAB’s svd command to obtain the singular values of A. How many are
# “large”? How many are “tiny”? (Use the command format short e to get a more
# accurate view of the singular values.) ## None of them are large. The largest is around 1, but there are two tiny ones that are 10^-16.
# c. Use MATLAB’s rank command to confirm that the numerical rank is 4.
# d. Use the rank command with a low enough threshold that it returns the value 6.
import numpy as np 
## This writes the random matrices. 
A = np.random.rand(8, 4) 
B = np.random.rand(4, 6)
matrix=np.dot(A, B)
print(matrix)

## Singular value of a matrix.
U, S, V = np.linalg.svd(matrix)
print("Singular values of the matrix:", S)

## Rank of a matrix
rank = np.linalg.matrix_rank(matrix)
print("Rank of the matrix:", rank)

## Rank of a matrix with a low threshold
rank_low = np.linalg.matrix_rank(matrix, tol=1e-10)
print("Rank of the matrix with low threshold:", rank_low)

