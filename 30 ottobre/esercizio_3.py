#Pagina: 72 -> https://www.canva.com/design/DAGNONH11dQ/ri6igYYiuYnxh6Sn77rmAA/edit

users = []

# Acquisisce i dati dall'utente
def req_data():
    username = input('Dammi il nome utente: ')
    password = input('Dammi la passwrod: ')
    # if(len(users)==0):
    #     register_user(username, password, 'admin')
    #     print('Sei il primo utente')
    return username, password

# Regista un utente
def register_user(username, password, auth='user'):
    is_ok = True
    for user in users:
        if user['username'] == username:
            is_ok = False
    if is_ok:
        users.append({'username': username, 'password': password, 'auth': auth})
    return is_ok
    

# Controlla se l'utente può accedere
def login(username, password):
    for user in users:
        if username == user['username'] and password == user['password']:
            return True
        else:
            return False

# Funzione dell'utente una volta loggato
def fibonacci():
    def req_number():
        return int(input('Dammi un numero: '))

    def F(i):
        if i == 1:
            return 1
        elif i == 2:
            return 1
        else:
            return F(i-1)+F(i-2)

    N = req_number()
    for i in range(1, N+1, 1):
        print(F(i))

# Eseguo il programma principale
if __name__ == '__main__':
    while True:
        nav = int(input('Nav: 0 register, 1 login, 2 esc: '))
        if nav == 0:
            res = False
            while  res ==False:
                username, password = req_data() # Riesta dati
                res = register_user(username, password)
        elif nav == 1:
            username, password = req_data() # Riesta dati
            accesso= login(username, password) # Controlla le credenziali
            if accesso: #Messaggio di avvenuto login
                print(f'\nHai effettuato l\'accesso "{username}", con la password "{password}"')
                fibonacci()
                nav = input('Vuoi effettuare il logout o uscire? (y/n): ')
                if nav == 'n' or nav == 'N':
                    print('\n')
                    break
            else:
                print('Accesso negato!')
                print('\n')
        elif nav == 2:
            break
        else:
            print('Scelta non valida!')
            print('\n')