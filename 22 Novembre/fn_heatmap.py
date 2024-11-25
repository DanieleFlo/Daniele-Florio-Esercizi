import pandas as pd
import numpy as np

def string_unique_split(df_temp, colonna):
    genres_list = set()
    df_temp.dropna(subset=colonna, inplace=True)
    for gen in df_temp[colonna]:
        for token in gen.split(','):
            genres_list.add(token.replace(' ', ''))
    genres_list= list(genres_list)
    return genres_list

# Converto un dataFrame in un formato per osserevare le correlazioni
def data_convet_to_heatmap(df_temp: pd.DataFrame, max_uniq=6, lista_colonne=None, min_corr=0.2):
    """
    Converte un dataframe in un formato per osservare le correlazioni
    
    Parameters:
    df_temp (pd.DataFrame): Dataframe da convertire
    max_uniq (int, optional): Massimo numero di valori unici per colonna. Default is 6.
    lista_colonne (list, optional): Lista delle colonne da considerare. Default is None (tutte le colonne).
    min_corr: valore oltre il quale la colonna non viene eliminata
    
    Returns:
    pd.DataFrame: Dataframe convertito
    """
    df_temp = df_temp.copy()
    if lista_colonne== None:
        lista_colonne = list(df_temp.columns.values)
    for colonna in lista_colonne:
        df_temp.dropna(subset=colonna, inplace=True)
        uniq = df_temp[colonna].unique()
        if ',' in uniq:
            uniq = string_unique_split(df_temp, colonna)
        
        # Se seno numeri non deve fare niente
        if issubclass(type(uniq[0]), np.float64) or issubclass(type(uniq[0]), np.int64)or issubclass(type(uniq[0]), np.int32):
            continue
        elif len(uniq)<=max_uniq and len(uniq)>1:
            # Se è lungo 2 la conversione è binaria
            if len(uniq)==2 or not issubclass(type(uniq[0]), str):
                df_temp[colonna] = df_temp[colonna].map({uniq[0]:0, uniq[1]:1})
                print(f'Converto {colonna} in 0 o 1')
            else:
                print(f'Converto {colonna} aggiungendo {len(uniq)} colonne, con valore 0 o 1')
                for u in uniq:
                    df_temp[colonna+'-'+u] = df_temp[colonna].apply(lambda x: 1 if u in x else 0)
                df_temp.drop(colonna, axis=1, inplace=True)
        else:
            print(f"Elimino: {colonna}, len: {len(uniq)}, {type(uniq[0])}")
            df_temp.drop(colonna, axis=1, inplace=True)
            
    lista_colonne_new = list(df_temp.columns.values)
    for colonna in lista_colonne_new:
        df_search = df_temp.corr()
        df_search[df_search[colonna]==1] =df_search[colonna].min()
        if df_search[colonna].min()>-min_corr and df_search[colonna].max()<min_corr:
            df_temp.drop(colonna, axis=1, inplace=True)
            print(f"Elimino colonna {colonna}, min: {df_search[colonna].min()}, max: {df_search[colonna].max()}")
    
    return df_temp