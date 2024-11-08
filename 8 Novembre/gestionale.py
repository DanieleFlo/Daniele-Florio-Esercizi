# Gestionale ripetibile ad oggett, login, registrazione -> controllo
# Funzionalità: punteggio 
# 0p -> somma: es. 6+6 res -> True 
# 5p -> somma: es. 6+6+6
# Classifica:
# - Stapare classifica
# - Salvare la classifica
# Metodo:
# 3 check ogni ora


# Gruppo:
# Pierfrancesco
# Pier Carlo
# Daniele


def io_classifica(stringa):
    file1 = open("classifica.txt", "w", encoding = "utf-8")

    # Writing multiple strings
    # at a time
    file1.writelines(stringa)

    # Closing file
    file1.close()



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
        username = input('Username: ')
        password = input('Password: ')
        res_name = self.__input(username)
        res_pass = self.__input(password)
        if res_name == True and res_pass ==True:
            user = self.__find_user(username)
            if user!=None:
                if self.__check_password(password, user.get_password()):
                    return True, user
            
        return False,
    
    # Aggiunge l'untete al dizionario
    def __add_user(self, username, password):
        user = User(username, password)
        self.__users[username] = user
    
    # Registrazione, controlla l'input e la password dell'utente ed aggiunge l'utente al dizionario se validi, altrimenti False
    def register(self):
        username = input('Username: ')
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
        res = self.__deconstructor(temp)
        return res
            
    def __deconstructor(self, dizionario):
        stringa = []
        for key, elemento in dizionario:
            parziale = f"Giocatore: {key} punteggio: {elemento} \n"
            stringa.append(parziale)
            
        return stringa

    

    
    
questions = [
    {"question": "Quanto fa 2 + 2?", "answer": 4},
    {"question": "Quanto fa 5 x 3?", "answer": 15},
    {"question": "La capitale della Francia?", "answer": "Parigi"},
    {"question": "Quanto fa 9 x 9?", "answer": 81},
    {"question": "Nome del cantante Bowie?", "answer": "Bowie"},
    {"question": "Quanto fa 50 / 5?", "answer": 10},
    {"question": "Quanto fa 7 x 8?", "answer": 56},
    {"question": "Quanto fa 144 / 12?", "answer": 12},
    {"question": "Quanto fa 19 + 21?", "answer": 40},
    {"question": "Quanto fa 100 - 37?", "answer": 63}
]

# Funzione per porre una domanda e controllare la risposta
def ask_question(level):
    question = questions[level - 1]["question"]
    correct_answer = questions[level - 1]["answer"]
    answer = input(question + " ")
    return answer == str(correct_answer)

# Funzione per giocare a un livello specifico
def play_level(level, user):
    print(f"Livello {level} ")
    if ask_question(level):
         user.set_score(float(user.get_score() + 1))
         print("Risposta corretta! Hai guadagnato 1 punto.")
         
    else:
        print("Risposta errata.")
    print(f"Punteggio attuale: {user.get_score()}")
    


# Funzione per mostrare i livelli disponibili
def show_available_levels(score):
    max_level = int(min(score + 1, 10))
    available_levels = list(range(1, max_level + 1))
    print("Livelli disponibili:", available_levels)
    return available_levels

# Funzione principale del gioco
def game():
    
    gestore_utenti = Users()
    print("Benvenuto nel Gioco di Matematica!")
    while True:
        action = input("Digita 'reg' per registrarti, 'login' per accedere, o 'esci' per uscire: ")
        if action.lower() == 'reg':
            result = gestore_utenti.register()
            if result:
                print("Registrazione avvenuta con successo!")
            else:
                print("Nome utente già in uso.")
                
            
        elif action.lower() == 'login':
            result = gestore_utenti.login()
            
            if result[0]:
                user = result[1]
                print(f"Accesso effettuato come {user.get_username()}!")
                while True:
                    # Mostra i livelli disponibili in base al punteggio
                    score = user.get_score()
                    available_levels = show_available_levels(score)
                    
                    # Permetti all'utente di scegliere un livello
                    chosen_level = input("Scegli un livello da giocare (o digita 'logout' per uscire): ")
                    if chosen_level.lower() == 'logout':
                        print("Logout effettuato.")
                        break
                    elif chosen_level.isdigit() and int(chosen_level) in available_levels:
                        play_level(int(chosen_level), user)
                    else:
                        print("Livello non valido o non sbloccato.")
            else:
                print("Nome utente o password non validi.")
        elif action.lower() == 'esci':
            print("Uscita dal gioco. Grazie per aver giocato!")
            lista = gestore_utenti.get_users_ord_score()
            output_string = ""
            for stringa in lista:
                output_string += stringa
            print(output_string)
            io_classifica(output_string)



        else:
            print("Comando non riconosciuto.")

# Avvio del gioco
if __name__ == "__main__":
    game()