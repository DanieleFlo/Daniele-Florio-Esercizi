# Login
# Azione -> Sfida matematica
# Classifica


"""
Andare a svolger e in gruppo minimo 3: Andiamo a creare un 
sistema a X fasi dove x è il numero dei partecipanti il cui 
scopo e: loggare, controllare i dati, far eseguire un "Gioco 
matematico a punteggio(numerico consiglio)" da cui creare un 
classifica e un logout con possibilità di ripetizione
"""

# Lista users (dizionario)

# Classe Utente
# User ->id (int), nome (string), password (string), punteggio (float)
# id -> crescente, (Attributo di classe)
"""Esempio:
    users = {
        0:{
            "nome": "",
            "punteggio": 0.0
        },
        1:{
            "nome": "",
            "punteggio": 0.0
        }
    }
    """

#Metodi
"""
    Menu inziale:
        1: Registrazione -> nome, password
        2: Login -> nome, password
        3: Exit
    
    Menu log.:
        1: Classifica
        2: Giocare
        3: Exit
    -----
    -> Registrazione: 
        - Aggiungere al dizionario e controlla se esiste -> se esiste ti da errore e va a login
        Output: nome, password, id <-(tupla)
        
    -> Login:
        - Controlla se esiste ed entra -> in caso di caso di errore password o nome sbagliato
        Output: result (boolean)
    
    -> Classifica
        - Stampa la classifica
        
    
    -> Giocare:
        - Va al gioco e rittorna un punteggi alla fine del gioco che va inserito nel dizionario all'utente che ha giocato
        Input: None,
        Output: Punteggio
        
        
        
    Task:
        Cosimo -> Login
        Stefano -> Gioco
        Roberta -> Registrazione
        Daniele -> Classifica

"""

users = {
    0:{
        "nome": "Marco",
        "punteggio": 1.0
    },
    1:{
        "nome": "Luca",
        "punteggio": 2.0
    }
}

# Ordina gli utentti in base al punteggio e stampa la classifica
def classifica():
    classifica_users = users.copy()
    classifica_users = sorted(classifica_users.items(), key=lambda item: list(item[1].values())[1], reverse=True)
    index = 1
    for user in classifica_users:
        print(f"{index}° posto: {user[1]["nome"]} -> {user[1]["punteggio"]}")
        index += 1

classifica()