#l'utente può inserire un alunno e i suoi voti in italiano e matematica, eliminare uno studente, 
# modificare un voto o uno studente, stampare tutti gli studenti e le loro medie


import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="prova_db"
)

"""
CREATE TABLE Autori (
    ID INT PRIMARY KEY,
    Nome VARCHAR(50)
);

CREATE TABLE Libri (
    ID INT PRIMARY KEY,
    Titolo VARCHAR(100)
);

CREATE TABLE Autori_Libri (
    AutoreID INT,
    LibroID INT,
    PRIMARY KEY (AutoreID, LibroID),
    FOREIGN KEY (AutoreID) REFERENCES Autori(ID),
    FOREIGN KEY (LibroID) REFERENCES Libri(ID)
);
"""

mycursor = mydb.cursor()

def create_table_studente():
     query = "CREATE Table IF NOT EXISTS Studenti (id int auto_increment primary key, Nome varchar(50), Voto_Italiano int, Voto_Matematica int)"
     mycursor.execute(query)


def insert_studente(nome, italiano, matematica):
    query = "INSERT INTO Studenti (Nome, Voto_Italiano, Voto_Matematica) VALUES (%s,%s,%s)"
    valori = (nome, italiano, matematica)
    mycursor.execute(query, valori)
    mydb.commit()
    print(mycursor.rowcount, "Studente inserito.")


def update_studente(ID,nome = None, italiano = None, matematica = None):
    if ID_Exsist(ID):
        if nome is not None:
            query = "UPDATE Studenti SET nome = %s WHERE id = %s"
            valori = (nome,ID)
            mycursor.execute(query, valori)
            mydb.commit()
            print(mycursor.rowcount, "Nome utente aggiornato.")
        elif italiano is not None:
            query = "UPDATE Studenti SET Voto_Italiano = %s WHERE id = %s"
            valori = (italiano,ID)
            mycursor.execute(query, valori)
            mydb.commit()
            print(mycursor.rowcount, "Voto italiano aggiornato.")
        elif matematica is not None:
            query = "UPDATE Studenti SET Voto_Matematica = %s WHERE id = %s"
            valori = (matematica,ID)
            mycursor.execute(query, valori)
            mydb.commit()
            print(mycursor.rowcount, "Voto matematica aggiornato.")
    else:
        print("Studente non trovato.")


def ID_Exsist(ID):
    query = "SELECT * FROM Studenti WHERE id = %s"
    valori = (ID,)
    mycursor.execute(query, valori)
    return mycursor.fetchone() is not None


def select_studente(id):
    if ID_Exsist(id):
        query = "SELECT * FROM Studenti WHERE id = %s"
        valori = (id,)
        mycursor.execute(query, valori)
        return mycursor.fetchone()
    else:
        return None

def delete_studente(id):
    if ID_Exsist(id):
        query = "DELETE FROM Studenti WHERE id = %s"
        valori = (id,)
        mycursor.execute(query, valori)
        mydb.commit()
        print(mycursor.rowcount, "Utente eliminato.")
    else:
        print("Studente non trovato.")


def select_all_studenti():
    query = "SELECT * FROM Studenti"
    mycursor.execute(query)
    return mycursor.fetchall()


def select_medie_alunni():
    query = "SELECT Nome,Voto_Italiano,Voto_Matematica,(Voto_Italiano + Voto_Matematica)/2 as Media FROM Studenti"
    mycursor.execute(query)
    return mycursor.fetchall()
    




while True:
    nav = input("Aggiungi alunno 1, aggiorna voto 2, rimuovi alunno 3, visualizza media alunni 4, esci 5: ")
    try:
        if nav == '1':
            nome = input("Dammi il nome: ")
            voto_italiano = int(input("Dammi il voto di italiano:"))
            voto_matematica = int(input("Dammi il voto di matematica:"))
            insert_studente(nome, voto_italiano, voto_matematica)
        elif nav == '2':
            print(select_all_studenti())
            indice = int(input("Dammi l'indice dello studente per modificare il voto: "))
            tipo_voto = input("Per aggiornare il voto di italiano seleziona 1, 2 per matetica: ")
            if tipo_voto == '1':
                voto_italiano = int(input("Dammi il nuovo voto di italiano:"))
                update_studente(indice, italiano=voto_italiano)
            elif tipo_voto == '2':
                voto_matematica = int(input("Dammi il nuovo voto di matematica:"))
                update_studente(indice, matematica=voto_matematica)
        elif nav == '3':
            print(select_all_studenti())
            indice = int(input("Dammi l'indice dello studente per rimuovere: "))
            delete_studente(indice)
        elif nav == '4':
            print(select_medie_alunni())
        elif nav == '5':
            break
        else:
            print("Scelta non valida!")
    except KeyError:
        print(KeyError)