#Create 2 array numpy:

# - Un array unidimensionale di numeri casuali compresi tra 0 e 1;
# - Un array bidimensionale di dimensione 3x3 con valori interi casuali.

import numpy as np

# Array unidimensionale

array_unidimensionale = np.random.random(10)
print(f"Unidimensionale shape: {array_unidimensionale.shape}; array:", array_unidimensionale)


array_bidimensionale = np.random.randint(low=0, high=2, size=(3,3))
print(f"\nBidimensionale shape: {array_bidimensionale.shape}; array:", array_bidimensionale)