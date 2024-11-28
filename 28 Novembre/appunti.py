import numpy as np
from scipy import linalg

A = np.array([[1,3], [2,4]])
b = np.array([6,8])

# Solve linear system Ax = b for x
x = linalg.solve(A, b)
print(x)
print(A[0,0]*x[0]+A[0,1]*x[1],'->',b[0])
print(A[1,0]*x[0]+A[1,1]*x[1],'->',b[1])