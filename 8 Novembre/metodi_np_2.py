import numpy as np


arr_3D = np.array([[1,2,3,4],
                   [5,6,7,8],
                   [9,10,11,12]])


print(arr_3D[2:3])
print()
print(arr_3D[: ,1:3])
print()
print(arr_3D[1: ,1:3])

prova = np.linspace(0, 5, 11)
print(prova.shape, prova)