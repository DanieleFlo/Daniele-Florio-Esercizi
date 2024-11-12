# Create 1 array unidimensionale con 50 valori randomici compresi tra 1 e 1.000 e 
# fate i seguenti calcoli:

# - Calcolo della media;
# - Calcolo della moda;
# - Calcolo della deviazione standard;
# - Trasformatelo in un array 5 X 10
import numpy as np
from scipy import stats

# Create array

arr = np.random.randint(1, 1000, 50)
print(arr)
print("Media")
print(np.mean(arr))
print("moda")
# print(dir(stats.mode(arr)))
mode_res = stats.mode(arr)
print(mode_res.mode)
print("deviazione standard")
print(np.std(arr))
print("Reshape")
print(arr.reshape((5,10)).shape)


