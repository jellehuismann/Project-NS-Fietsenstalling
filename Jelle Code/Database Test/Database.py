import sqlite3
Naam = 'aaa'
Achternaam = 'aaa'
Adress = 'aaa'
FietsNr = 2343
PIN = 3343
otpKEY = 'aaa'

db_conn = sqlite3.connect('database.db')
dbcursor = db_conn.cursor()

def create_table():
    db_conn.execute('CREATE TABLE IF NOT EXISTS Fietsenstalling (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, '
                    'Naam TEXT ,Achternaam TEXT ,Adress TEXT ,Telefoon INTEGER ,FietsNr INTEGER ,PIN INTEGER ,otpKEY TEXT)')
    dbcursor.commit()
print(create_table())

def printdb():
    try:
        Result = db_conn.execute("SELECT ID, Name, FietsNr FROM Fietsenstalling")
        for row in Result:
            print("ID :", row[0])
            print("Name :", row[1])
            print("FietsNr :", row[2])
    except sqlite3.OperationalError:
        return "The table doesn't Exist"

db_conn.execute("INSERT INTO Fietsenstalling (Naam, Achternaam, Adress, FietsNr, PIN, otpKEY) VALUES "
                "(?, ?, ?, ?, ?, ?);",(Naam, Achternaam, Adress, FietsNr, PIN, otpKEY))

db_conn.close()
