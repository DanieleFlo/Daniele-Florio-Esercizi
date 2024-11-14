import mysql.connector

"""
# Connessione al DB
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
)

print(mydb)
print('Info:')
print('Port:', mydb._port)
print('Conn.:',mydb.is_connected())
print('Vers.:',mydb.get_server_info())

def show_dbs():
    global mycursor
    # Mostra i database presenti nel DB
    mycursor.execute("SHOW DATABASES")
    print('\nLista DB:')
    for x in mycursor:
        print(x)
        
# Cursore per interagire con il DB
mycursor = mydb.cursor()

show_dbs()
try:
    qurey = "create database prova_db"
    mycursor.execute(qurey)
    show_dbs()
except:
    pass
"""

# Connessione al DB
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="prova_db"
)

print(mydb)
print('Info:')
print('Port:', mydb._port)
print('Conn.:',mydb.is_connected())
print('Vers.:',mydb.get_server_info())

mycursor = mydb.cursor()


# Crea una tabella 'utenti' con due campi: nome e indirizzo
# query = 'create table utenti (nome varchar(50), indirizzo varchar(50))'

# Elimina la tabella
# query = 'drop table utenti '
# mycursor.execute(query)

# Mostra le tabelle
# query = 'show tables'

# mycursor.execute(query)
# for x in mycursor:
#     print(x)

# Tabella con valori reali
# query = 'create table utenti (id int auto_increment primary key, nome varchar(50), indirizzo varchar(50))'
# mycursor.execute(query)

# Mostra le tabelle
# query = 'show tables'

# mycursor.execute(query)
# for x in mycursor:
#     print(x)

# # Inserisco 1 utente
# query = 'insert into utenti (nome, indirizzo) values(%s,%s)'

# valori = 'mario', 'boh'

# mycursor = mydb.cursor()
# mycursor.execute(query, valori)

# mydb.commit()

# print(mycursor.rowcount, 'record inserted.')

# # Inserisco 1 utente
# query = 'insert into utenti (nome, indirizzo) values(%s,%s)'

# valori = [('Giorgio', 'boh2'),
#           ('Franco', 'boh3')]


# mycursor.executemany(query, valori)

# mydb.commit()

# print(mycursor.rowcount, 'record inserted.')

# Vediamo il select

# query = 'select * from utenti'
# mycursor.execute(query)

# query = 'select * from utenti where nome=%s'
# query = 'delete from utenti where nome=%s'
# nome = "mario",
# mycursor.execute(query,nome)
# mydb.commit()
# print(mycursor.rowcount, 'record delete.')

# Ritorna titti
# result = mycursor.fetchall()
# for x in result:
#     print(x)

# #Ritorna il primo
# result = mycursor.fetchall()
# print(result)
