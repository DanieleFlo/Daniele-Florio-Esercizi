"""
Pandas e Numpy e Visualizzazione 
Descrizione: Crea un dataset autogenerandolo monolineare con 50 posizioni matematica e cambia la sua forma in 10 file da 5, 
normalizza i valori e rendili interi , nessun valore deve essere uguale a un altro sulla stessa linea della collezione  
dopodiché stampa un grafico che lo rappresenti. 
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
max_val = 100
min_val = 1
N = 50
# Creazione del dataset
dataset = np.random.uniform(min_val, max_val, N)
print('Dataset:', dataset)

# Rendo interi tutti i numeri (normalizzo allo stesso tipo)
dataset_norm = dataset.astype(np.int32)
print('Normalizzo allo stesso tipo:', dataset_norm)
dataset_norm_reshape = dataset_norm.reshape((10,5))
print('Reshape:', dataset_norm_reshape)

print()
# Scorro su ogni riga e verifico eventuali duplicati
for i in range(dataset_norm_reshape.shape[0]):
    # Prendo i valori unici nella riga
    uniq_line = np.unique(dataset_norm_reshape[i])
    if len(uniq_line) != 5:
        # Genera un nuovo valore casuale per l'elemento duplicato
        max_in_line = np.max(uniq_line) # prendo il valore massimo
        temp = uniq_line.copy() # creo un array temporane con i valori uinici
        for j in range(5-len(uniq_line)):
            temp = np.append(temp, max_in_line+j+1) # aggiungo 1 più la distanza di quanto manca a completare la riga
        dataset_norm_reshape[i] = temp # Sostituisco la lista con solo valori unici nell'array

print('Dataset con valori unici su ogni riga',dataset_norm_reshape)


# Creo il grafico in gruppi in base alla riga
n_rows, n_cols = dataset_norm_reshape.shape
x = np.arange(n_rows)  # Indici delle righe
width = 0.15  # Larghezza delle barre
colors = plt.cm.viridis(np.linspace(0, 1, n_cols))  # Colori per le colonne

# Grafico
fig, ax = plt.subplots(figsize=(10, 6))

for i in range(n_cols):
    ax.bar(x + i * width, dataset_norm_reshape[:, i], width, label=f'C. {i+1}', color=colors[i])

# Etichettatura e miglioramenti
ax.set_xlabel('Righe')
ax.set_ylabel('Valori')
ax.set_title('Grafico a Gruppi di Barre per Righe')
ax.set_xticks(x + (n_cols - 1) * width / 2)
ax.set_xticklabels([f'Riga {i+1}' for i in range(n_rows)])
ax.legend(title="Colonne")
ax.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()