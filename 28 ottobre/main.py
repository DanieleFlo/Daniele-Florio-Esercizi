# nome = input("Inserisci il tuo nome:")
# eta = int(input("Inserisci la tua età:"))
# print("Ciao, "+ nome +"! Benvenuto in Python")

# print(2+1)

# s = "Python"
# print(s[0])
# print(s[2])

# saluto = "Ciao"
# nome = "Alice"
# messaggio = saluto + " " + nome

# print(messaggio)

# s = "Ciao, mondo!"
# print(len(s))
# print(s.upper())
# print(s.lower())
# print(s.split(","))
# print(s.replace("mondo", "universo"))

# x = 5
# y = 10
# print(x==y)
# print(x!=y)
# print(x<y)

# nome = input("Inserisci un nome: ")
# nome_dim = len(nome)
# # print(nome[-1])
# print("Ultima lettera: " + nome[nome_dim-1])

#Liste
# numeri  = [3,4,6,2,72,1]
# print(numeri)
# print(len(numeri))
# numeri.append(8)
# print(numeri)
# numeri.insert(0, 8)
# print(numeri)
# numeri.remove(3)
# print(numeri)
# numeri.pop(2)
# print(numeri)
# numeri.sort()
# print(numeri)
# numeri.sort(reverse=True)
# print(numeri)


#Tuple
"""
punto = 3,4
print(type(punto))
"""

#Dizionari
"""
persona = {
    "nome": "Alice",
    "eta": 25,
    "cognome": "Smith",
    "citta": "New York"
}
print(type(persona))
print(persona["nome"])
print(persona.get("nonesiste"))
print(persona)
persona["altezza"] =1.59
print(persona)
print(persona.keys())
print(list(persona.keys())[0])
print(persona.values())
print(list(persona.values())[0])
print(persona.items())
"""


#Esercizio
"""
boleano = bool(int(input("Boleano: ")))
# boleano = bool(i(input("Boleano: ")))
intero = int(input("Intero: "))
s = input("Stringa: ")

lista = [boleano, intero, s]

espempio_dict = {
    "tipi_di_dato": lista
}

print(espempio_dict)
"""

#Insiemi (set)
"""
set1 = set([1,2,3,4,5])
set2 = {4,5,6,7,8}
print(type(set1))
print(set2)
print(set1)

print(set1.union(set2)) #Unisce gli insiemi o |  
print(set1 & set2) #Intersezione fra gli insiemi
print(set1 - set2) #Differenza del primo insieme rispettto al secondo
print(set1 ^ set2) #Unione senza l'intesezione
"""

#Esercisio
"""
numero = int(input("Numero: "))
if numero % 2:
    print("Il numero è dispari")
else:
    print("Il numero è pari")
"""


#Esercizio
"""
def control_years(anno):
    return (anno%4==0 and anno%100!=0) or anno%400==0 

anno = int(input('Dammi un anno:'))

if control_years:
    print(anno, 'è un anno bisestile')
else:
    print(anno, 'non è un anno bisestile')
"""

#Esercizio Login
"""
user = {
    "username": "admin",
    "password": "1234",
    "res_1": "rosso",
    "res_2": "coniglio" 
}

username_input = input("Username: ")
password_input = input("Password: ")


def control_login(username, password):
    if username != user["username"] or password != user["password"]:
        return "Accesso negato!"
    print("Accesso consentito!")

    change_password = input("Vuoi cambiare password? (yes/no): ")
    if change_password.lower() !='yes' and change_password.lower() != 'y':
        return 'Non vuoi cambiare password'
    
    question_choise = int(input("Domanda di sicurezza: colore o animale preferito (1/2): "))
    res = ''
    if question_choise == 1:
        res = input('Colore preferito?:').lower()
    else:
        res = input('Animale preferito?:').lower()

    if (res==user["res_1"] and question_choise==1) or (res==user["res_2"] and question_choise==2):
        user["password"] = input('Dimmi la nuova password:')
        return 'La tua nuova password è:' + user["password"]
    else:
        return 'La risposta non è corretta'

print(control_login(username_input, password_input))
"""


#Esercizio
products = [{
    'name': 'Farina',
    'price': 10.99
},
    {
    'name': 'Uova',
    'price': 5.99
},
    {
    'name': 'Miele',
    'price': 1900.00
},]

acquisti = []
acquisti.append(products[0])

user = {}

print("Effettua la registrazione:")
new_username = input("Username: ")
new_password = input("Password: ")

if new_username !='admin':
    user['username'] = new_username
    user['password'] = new_password
else:
    print("Non puoi registrarti come admin")
    exit()

print("\nEffettua il login:")
username = input("Username: ")
password = input("Password: ")
if username == 'admin' and password == 'password':
    print("Accesso come admin")
    visualizza_admin = input("\nVuoi visualizzare i prodotti?(Yes|No): ")
    if visualizza_admin.lower() == 'yes' or visualizza_admin.lower()=='y':
        print('-Lista prodotti:', products)
    nav_admin = int(input('Aggiungi articolo premi 1, rimuovi 2: '))
    if nav_admin == 1:
        new_product = {}
        new_product['name'] = input("Nome: ")
        new_product['price'] = float(input("Prezzo: "))
        products.append(new_product)
        print("Prodotto aggiunto con successo!\n")
    if nav_admin == 2:
        pos = int(input("Posizione del prodotto da rimuovere: "))
        products.pop(pos)
    
    print('-Lista prodotti:', products)
        
elif username == user['username'] and password == user['password']:
    print("Accesso come utente\n")
    visualizza_prod = input("Vuoi visualizzare i prodotti?(Yes|No): ")
    if visualizza_prod.lower() == 'yes' or visualizza_prod.lower()=='y':
        print('-Lista prodotti:', products)
    visualizza_prod = input("\nVuoi visualizzare gli acquisti?(Yes|No): ")
    if visualizza_prod.lower() == 'yes' or visualizza_prod.lower()=='y':
        print('-Lista acquizi:', acquisti)
    nav_user = int(input('\nAggiungi alla lista acquisti premi 1, rimuovi 2: '))
    if nav_user == 1:
        pos = int(input("Posizione del prodotto da aggiungere alla lista acquisti: "))
        acquisti.append(products[pos])
        print("Prodotto aggiunto con successo!")
    if nav_user == 2:
        pos = int(input("Posizione del prodotto da rimuovere: "))
        acquisti.pop(pos)

    print('\n-Lista acquizi:', acquisti)
else:
    print("\nAccesso negato")