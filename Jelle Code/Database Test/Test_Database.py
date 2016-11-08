import sqlite3

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
              'Name TEXT, Adress TEXT, FietsNr INTEGER, PIN INTEGER, otpKEY TEXT)')
    except AttributeError:
        return 'Database is niet juist bijgewerkt controleer de database of controleer de code!'
db.execute("INSERT INTO Fietsenstalling (Name, Adress, FietsNr, PIN, otpKEY) VALUES "
           "('Gandalf', 'Shire 223','7584','3243','afmeyhdh7sqqoimr')")

print(controle)
print(create_table())
printdb()


