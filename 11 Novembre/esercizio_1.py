# 1 - Generare 5 numeri causali e scriverli in un file
# 2 - Leggere il file e l'utente deve indovinare 
# almeno due numeri dei 5 presenti

from random import randint

MAX = 10
MIN = 1
N = 5

# Scrivo il file
with open("./11 Novembre/esercizio_1.txt", 'w') as f:
    f.write('\t'.join([str(randint(MIN, MAX)) for _ in range(N)]))

contenuto = ''
with open("./11 Novembre/esercizio_1.txt", 'r') as f:
    contenuto = f.read()
    
contenuto = contenuto.split('\t')
    
try:
    contenuto = list(map(int, contenuto))
except:
    contenuto = []
    print("Errore durante la conversione dei numeri.")


if len(contenuto)>0:
    indovinati = 0
    tentativi = 0
    while True:
        print(f"Indovina i numeri tra {MIN} e {MAX}. Hai {5-tentativi} {"tentativo" if (5-tentativi)==1 else "tentativi"}.")
        for i, num in enumerate(contenuto):
            print(f"{i+1}. {num}")
        
        try:
            n = int(input("Gioca: "))
            if n<MIN or n>MAX:
                print("Numero non valido.")
            else:
                tentativi +=1
                if n in contenuto:
                    contenuto.remove(n)
                    indovinati += 1
                    if 2-indovinati>0:
                        print(f"Bravo! Hai indovinato il numero. Ne restano: {2-indovinati}")
                    if indovinati >=2:
                        print(f"Hai vinto!")
                        break
                else:
                    if tentativi>4:
                        print(f"Hai perso!")
                        break
                    print("Numero non presente. Riprova.")
        except ValueError:
            print("Numero non valido")
        
else:
    print("Errore durante il caricamento del file.")
    

        