# Esercitazione sullo slicing e F. Indexing
import numpy as np

class SlicingAndIndexing():
    def __init__(self):
        self._array = np.array([])
        self._array_mod =  []
    
    def create_array(self, start, stop, size):
        self._array = np.random.randint(start, stop, size)
        self.get_array()
    
    def get_array(self):
        print("Array")
        print(self._array.shape, self._array)
        return self._array
        
    def estrai_primi(self, n):
        print(f"Primi {n}")
        print(self._array[:n])
        self._array_mod.append(self._array[:n])
        
    def estrai_ultimi(self, n):
        print(f"Ultimi {n}")
        print(self._array[-n:])
        self._array_mod.append(self._array[-n:])
        
    def estrai_index(self, start, stop):
        print(f"Index inizio: {start}, fine: {stop}")
        temp = np.arange(start, stop-1)
        print(self._array[temp])
        self._array_mod.append(self._array[temp])
        
    def estrai_el(self, pos):
        print(f"Estrai alla posizione {pos}")
        for arr in self._array_mod:
            print(arr[pos])
        
    def mod_index(self, start, stop, value):
        print(f"Mod {start} {stop} con {value}")
        temp = np.arange(start, stop-1)
        self._array[temp] = 99
        print(self._array)
    
    def get_arr_bod(self):
        print("Array modificati")
        for arr in self._array_mod:
            print(arr)

    def stampa(self):
        self.get_array()
        self.get_arr_bod()
        

es = SlicingAndIndexing()
es.create_array(10,50,20)
print()
es.estrai_primi(10)
print()
es.estrai_ultimi(5)
print()
es.estrai_index(5,15)
print()
es.estrai_el(3)
print()
es.mod_index(5,10, 99)
print()
es.stampa()