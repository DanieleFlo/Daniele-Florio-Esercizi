# Create un programma di gestione scolastica che utilizza un file txt 
# come database, potrete aggiungere o eliminare un alunno e i suoi voti


file_path = 'alunni.txt'

# Fa la media di una lista di voti
def media_voti(voti):
    voti = list(map(int, voti))
    return sum(voti) / len(voti) if len(voti) > 0 else 0

def aggiungi_alunno(file_path, nome, cognome, voti): 
    with open(file_path, 'a', encoding='utf-8') as file: 
        file.write(f"{nome}:{cognome}:{','.join(map(str, voti))}\n") 
        print(f"Alunno {nome} {cognome} aggiunto con voti {voti}.")


def stampa_media(lista):
    for alunno in lista:
        print(f"{alunno[0]} {alunno[1]} - Media voti: {media_voti(alunno[2])}")




# Crea lista voti
def aggiungi_voti():
    voti = []
    while True:
        nav2 = input("Dammi un vot 1, esci 2: ")
        if nav2 == '1':
            voti.append(input("Voto: "))
        else:
            break
    return voti

def salva_alunni(lista_alunni):
    # Pulisce il file
    with open(file_path, 'w', encoding='utf-8') as file: 
        file.write("")
        
    # Aggiungo la lista aggiornata
    for alunno in lista_alunni:
        aggiungi_alunno(file_path, alunno[0], alunno[1], alunno[2])

def stampa_lista(lista):
    for alunno in lista:
        print(f"{alunno[0]} {alunno[1]} - Voti: {alunno[2]}")
        
def visualizza_alunni(file_path):
    with open(file_path, 'r', encoding='utf-8') as file: 
        righe = file.readlines() 
        for riga in righe: 
            nome, cognome, voti = riga.strip().split(':') 
            voti = voti.split(',') 
            print(f"Alunno: {nome} {cognome}, Voti: {voti}")
        
def leggi_alunni(file_path):
    lista_alunni = []
    with open(file_path, 'r', encoding='utf-8') as file: 
        righe = file.readlines() 
        for riga in righe: 
            nome, cognome, voti = riga.strip().split(':')
            voti = voti.split(',') 
            lista_alunni.append([nome,cognome,voti])
    return lista_alunni
    
while True:
    nav = input("Aggiungi alunno 1, aggiungi voto 2, rimuovi alunno 3, visualizza alunni 4, rimuovi voto 5, aggiorna alunno 6, esci 7: ")
    try:
        if nav == '1':
            nome = input("Dammi il nome: ")
            cognome = input("Dammi il cognome: ")
            voti = aggiungi_voti()
            aggiungi_alunno(file_path, nome, cognome, voti)
            visualizza_alunni(file_path)
        elif nav == '2':
            lista_alunni = leggi_alunni(file_path)
            stampa_lista(lista_alunni)
            index = int(input("Dammi il l'indice: "))
            alunno = lista_alunni[index-1]
            new_voti = aggiungi_voti()
            alunno[2].extend(new_voti)
            salva_alunni(lista_alunni)
        elif nav == '3':
            lista_alunni = leggi_alunni(file_path)
            stampa_lista(lista_alunni)
            index = int(input("Dammi il l'indice: "))
            lista_alunni.pop(index-1)
            salva_alunni(lista_alunni)
        elif nav == '4':
            lista_alunni = leggi_alunni(file_path)
            stampa_media(lista_alunni)
        elif nav == '5':
            lista_alunni = leggi_alunni(file_path)
            stampa_lista(lista_alunni)
            index = int(input("Dammi il l'indice: "))
            print("Voti disponibili dell'alunno: ",lista_alunni[index-1][2])
            index_voto = int(input("Dammi il l'indice del voto: "))
            lista_alunni[index-1][2].pop(index_voto-1)
            salva_alunni(lista_alunni)
            print("Lista di tutti gli alunni: ")
            visualizza_alunni(file_path)
        elif nav == '6':
            lista_alunni = leggi_alunni(file_path)
            stampa_lista(lista_alunni)
            index = int(input("Dammi il l'indice: "))
            print("Vuoi aggiornare nome o cognome?: ",lista_alunni[index-1])
            index_aggiorna = int(input("1 per nome, 2 per cognome: "))
            lista_alunni[index-1][index_aggiorna-1] = input("Inserisci il nuovo valore: ")
            salva_alunni(lista_alunni)
            print("Lista di tutti gli alunni: ")
            visualizza_alunni(file_path)
        elif nav == '7':
            break
        else:
            print("Scelta non valida!")
    except:
        print("Scelta non valida!")



# l'utente deve poter:
# - aggiungere, rimuovere o aggiornare voti
# - aggiungere, rimuovere o aggiornare alunno
# - aggiungere la possibilità di stampare nome alunno e sua media