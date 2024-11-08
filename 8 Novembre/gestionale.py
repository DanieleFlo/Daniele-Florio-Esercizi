# Gestionale ripetibile ad oggett, login, registrazione -> controllo
# Funzionalità: punteggio 
# 0p -> somma: es. 6+6 res -> True 
# 5p -> somma: es. 6+6+6
# Classifica:
# - Stapare classifica
# - Salvare la classifica
# Metodo:
# 3 check ogni ora


#


class User():
    def __init__(self, username, password, score=0):
        self.__username = username
        self.__password = password
        self.__score = score
    
    def get_username(self):
        pass
    
    def get_password(self):
        pass
    
    def get_score(self):
        return self.__score
    
    def set_score(self, new_score : int):
        pass
    
    
class Users():
    __id = 0
    def __init__(self, username, password, score=0):
        super().__init__(username, password, score)
        self.__users = []
    
    def __check_password(self, password: str, users: list):
        for user in users:
            if self.__password == user["username"]:
                pass
    
    def login(self, username: str, password: str):
        pass
    
    def register(self, username: str, password: str):
        pass
    
    
    