# Create 2 array bidimensionali numpy 4x4 con valori interi casuali ed 
# eseguite le seguenti operazioni:

# - Restituite la somma di tutti gli elementi dei singoli array 
# che si trovano nell'ultima riga dalla seconda colonna in poi;
# - Unite i 2 array secondo l'asse 1.
import numpy as np

shape = 4,4

array_1 = np.random.randint(low=0, high=8, size=shape)
array_2 = np.random.randint(low=0, high=5, size=shape)
print("array 1")
print(array_1)
print("array 2")
print( array_2)

# Unione lungo asse 1
print("Unione lungo asse 1")
print(np.concatenate((array_1, array_2), axis=1))

print("Somma")
print(np.sum(array_1[-1,1:]), np.sum(array_2[-1,1:]))
print(array_1[-1,1:]+array_2[-1,1:])
print(np.sum(array_1[-1,1:]+array_2[-1,1:]), "=", np.sum(array_1[-1,1:]), "+", np.sum(array_2[-1,1:]))