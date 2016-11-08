import sqlite3
Naam = 'aaa'
Achternaam = 'aaa'
Adress = 'aaa'
FietsNr = 'aaa'
PIN = 'aaa'
otpKEY = 'aaa'

connect = sqlite3.connect('database.db')
db = connect.cursor()
def printdb():
    try:
        Result = db.execute("SELECT ID, Name, FietsNr FROM Fietsenstalling")
        for row in Result:
            print("ID :", row[0])
            print("Name :", row[1])
            print("FietsNr :", row[2])
    except sqlite3.OperationalError:
        return "The table doesn't Exist"

def create_table():
    try:
        db.execute('CREATE TABLE IF NOT EXISTS Fietsenstalling (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, '
              'Naam TEXT ,Achternaam TEXT ,Adress TEXT ,Telefoon INTEGER ,FietsNr INTEGER ,PIN INTEGER ,otpKEY TEXT)')
    except AttributeError:
        return 'Database is niet juist bijgewerkt controleer de database of controleer de code!'
print(create_table())

db.execute("INSERT INTO Fietsenstalling (Naam, Achternaam, Adress, FietsNr, PIN, otpKEY) VALUES (?, ?, ?, ?, ?, ?);",(Naam, Achternaam, Adress, FietsNr, PIN, otpKEY))



