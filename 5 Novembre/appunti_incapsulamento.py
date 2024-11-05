#Incapsulamento

class Computer():
    def __init__(self):
        self.__processore = "intel i5"
    
    def get_processore(self):
        return self.__processore
    
    def set_processore(self, new_processore):
        self.__processore = new_processore
        
pc = Computer()
print(pc.get_processore())
pc.set_processore("AMD Ryzen 5")
print(pc.get_processore())