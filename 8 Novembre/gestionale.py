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
        return self.__username
    
    def get_password(self):
        return self.__password
    
    def get_score(self):
        return self.__score
    
    def set_score(self, new_score : float):
        if isinstance(new_score, float) and new_score>0:
            self.__score = new_score
    
 
class Users():
    
    def __init__(self):
        self.__users = {}
    
    # Verifica che l'input sia valido, 0<stringa<20
    def __input(self, data: str):
        if isinstance(data, str) and len(data)>0 and len(data)<20:
            return True
        else:
            return False
    
    # Verifica che le password siano concordi
    def __check_password(self, password: str, password_user:str):
            if password_user == password:
                return True
            else:
                return False
    
    # Verifica che l'utente esite
    def __find_user(self, username):
        for key in self.__users.keys():
            if key == username:
                return self.__users[username]
        return None
    
    # Login, controlla l'input e la password dell'utente ed ritorna True, l'utente in caso di affermativo, altrimenti False
    def login(self):
        username = input('Usernname: ')
        password = input('Password: ')
        res_name = self.__input(username)
        res_pass = self.__input(password)
        if res_name == True and res_pass ==True:
            user = self.__find_user(username)
            if user!=None:
                if self.__check_password(password, user.get_password()):
                    return True, user
            
        return False 
    
    # Aggiunge l'untete al dizionario
    def __add_user(self, username, password):
        user = User(username, password)
        self.__users[username] = user
    
    # Registrazione, controlla l'input e la password dell'utente ed aggiunge l'utente al dizionario se validi, altrimenti False
    def register(self):
        username = input('Usernname: ')
        password = input('Password: ')
        res_name = self.__input(username)
        res_pass = self.__input(password)
        if res_name == True and res_pass ==True:
            user = self.__find_user(username)
            if user==None:
                self.__add_user(username, password)
                return True
        return False
    
    def get_users_ord_score(self):
        temp = {}
        for key, user in self.__users.items():
            temp[key] = user.get_score()
            self.__users[key].get_score()
        temp = sorted(temp.items(), reverse=True)
        print(temp)
        res = self.__deconstructor(temp)
        return res
            
    def __deconstructor(self, dizionario):
        stringa = ""
        for key, elemento in dizionario:
            parziale = f"Giocatore: {key }punteggio: {elemento}"
            stringa += parziale
        return stringa

    
    
users = Users()
print(users.register())
print(users.login())
print(users.register())
print(users.get_users_ord_score())