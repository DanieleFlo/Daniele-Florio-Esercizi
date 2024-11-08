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
        self._array[temp] = value
        print(self._array)
    
    def get_arr_bod(self):
        print("Array modificati")
        for arr in self._array_mod:
            print(arr)

    def stampa(self):
        self.get_array()
        self.get_arr_bod()
        

es = SlicingAndIndexing()
class Gestione():
    def __init__(self):
        pass
    @staticmethod
    def input(msg, opzioni=False, msg_error='Scelta non valida!'):
        if opzioni!=False and isinstance(opzioni[0], int):
            val = input(msg +': ')
            if val.isdigit():
                new_val = int(val)
                if opzioni==False or new_val in opzioni:
                    return new_val
                else:
                    print(msg_error)
            else:
                print(msg_error)
        elif opzioni==False or isinstance(opzioni[0], str):
            val = input(msg +': ')
            if val!= '':
                if opzioni==False or val in opzioni:
                    return val
                else:
                    print(msg_error)
            else:
                print(msg_error)
        else:
            print('tipo di input non valido')
        return None
                

while True:
    print("\n--Menu--")
    print("1. Crea array")
    print("2. Estrai i primi n")
    print("3. Estrai gli ultimi n")
    print("4. Estrai da un indice a un altro")
    print("5. Estrai da una posizione")
    print("6. Modifica da un indice a un altro con valore")
    print("7. Stampa array modificati")
    print("8. Esci")
    scelta = Gestione.input('->', ['1', '2', '3', '4', '5', '6', '7', '8'])
    if scelta=='1':
        start = int(input('start: '))
        end = int(input('end: '))
        n = int(input('N: '))
        print()
        es.create_array(start,end,n)
    elif scelta=='2':
        n = int(input('N primi: '))
        print()
        es.estrai_primi(n)
    elif scelta=='3':
        n = int(input('N ultimi: '))
        print()
        es.estrai_ultimi(n)
    elif scelta=='4':
        start = int(input('start index: '))
        end = int(input('end index: '))
        print()
        es.estrai_index(start, end)
    elif scelta=='5':
        n = int(input('Pos: '))
        es.estrai_el(n)
        print()
    elif scelta=='6':
        pass
    elif scelta=='7':
        start = int(input('start: '))
        end = int(input('end: '))
        n = int(input('Value: '))
        print()
        es.mod_index(start,end,n)
    elif scelta=='8':
        break