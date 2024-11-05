# Scrivete un programma che prenda i nomi degli alunni di una
# classe e i loro voti, quando l’utente scrive media il programma
# andrà a stampare i nomi di tutti gli alunni e per ogni alunno la
# media dei voti.
# Esempio:
# Nome: Giovanni , Media: 7.5
# Nome: Alfredo , Media: 9
# Nome: Michela, Media 10

# Lista per salvare gli alunni
alunni = []

#Funzione che fa aggiungere i voti
def add_voto():
    voti  = []
    while True:
        nav = (input("Vuoi aggiungere un voto? (y/n): ")).lower()
        if nav == "y":
            voto = input("Voto: ")
            if not voto.isdigit():
                print("Il voto deve essere un numero!")
            else:
                voti.append(float(voto))
        elif nav == "n":
            if len(voti)==0:
                print("\nDevi aggiungere almeno 1 voto!\n")
            else:
                break
        else:
            print("Scelta non valida!")
    return voti
        
#Funzione che aggiunge un alunno
def aggiungi_alunno():
    nome = input("Nome alunno: ")
    voti = add_voto()
    alunni.append({"nome": nome, "voti": voti})

#Funzione che stampa gli alunni e calcola la loro media
def stampa_alunni():
    if(len(alunni)!=0):
        print('')
        for alunno in alunni:
            media = sum(alunno["voti"]) / len(alunno["voti"])
            print(f"Nome: {alunno['nome']}, Media: {media}")
        print('')
    else:
        print("\nNon ci sono alunni!\n")


while True:
    nav = (input("Aggiungi alunno -> y\nrisultato con media -> media\nesci -> exit\n-> ")).lower()
    if nav=="exit":
        break
    elif nav=="y":
        aggiungi_alunno()
    elif nav=="media":
        stampa_alunni()
    else:
        print("Scelta non valida!")