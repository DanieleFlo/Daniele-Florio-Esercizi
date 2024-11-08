import numpy as np


arr = np.array([True, '', 3, 4])

arr2  = np.array([[1,2,3,4], [1,2,3,4]])

# print(arr.dtype)
# print(arr.size)
# print(arr2.size)
# print(f'Array 1: {arr}, shape: {arr.shape}, ndmi: {arr.ndim}')
# print(f'Array 2: {arr2}, shape: {arr2.shape}, ndmi: {arr2.ndim}')


arr3 = np.arange(0, 3, 0.5)
# print(arr3, arr3.shape)
arr3 = arr3.reshape(6,1)
# print(arr3)

class Boh():
    def __init__(self, esempio_array):
        self._esempio_array = esempio_array
        
    def trasfroma_to_float(self):
        return self._esempio_array.astype(np.float64)
    

esempio_array = np.arange(10, 49)
print(esempio_array.dtype)
boh = Boh(esempio_array)
esempio_array = boh.trasfroma_to_float()
print(esempio_array.dtype)
print(esempio_array)

# esempio_array = 
# print(esempio_array.dtype)

# esempio_array =  np.array(esempio_array, dtype=np.float64)
# print(esempio_array.dtype)