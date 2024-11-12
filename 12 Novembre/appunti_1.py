"""
import pickle

dizionario = {
    "nome": "Daniele",
    "cognome": "Florio",
    "eta": 30
}

# dizionarioB = pickle.dump(dizionario) # Alternativa

with open("12 Novembre/prova.pkl", "wb") as f: # wb Scrivoin binario
    pickle.dump(dizionario, f)


with open("12 Novembre/prova.pkl", "rb") as f: # Leggi in binario
    countenuto = pickle.load(f)

print(type(countenuto))
print(countenuto["nome"], countenuto["cognome"], countenuto["eta"])
"""