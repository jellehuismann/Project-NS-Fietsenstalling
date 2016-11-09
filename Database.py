import sqlite3
import sys

Naam = 'bbb'
Achternaam = 'aaa'
Adress = 'aaa'
FietsNr = 2343
PIN = 3343
otpKEY = 'aaa'

db_conn = sqlite3.connect('database.db')

print("Database Created")

theCursor = db_conn.cursor()
#Database aanmaken
def print_database():
    try:
        result = theCursor.execute("SELECT ID, Naam, Achternaam, Adress, Telefoon, FietsNr, PIN, otpKEY FROM Fietsenstalling")

        # You receive a l`ist of lists that hold the result
        for row in result:
            print("Naam :", row[0])
            print("Achternaam :", row[1])
            print("Adress :", row[2])
            print("Telefoon :", row[3])
            print("FietsNr :", row[4])
            print("PIN :", row[5])
            print("otpKEY :", row[6])

    except sqlite3.OperationalError:
        print("The Table Doesn't Exist")

    except:
        print("Couldn't Retrieve Data From Database")

def create_database():
    """
    Functie om een database Tabel aan te maken.
    """
    try:
        db_conn.execute('CREATE TABLE IF NOT EXISTS Fietsenstalling (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, '
                        'Naam TEXT ,Achternaam TEXT ,Adress TEXT ,Telefoon INTEGER ,FietsNr INTEGER ,PIN INTEGER ,otpKEY TEXT)')
        db_conn.commit()
        print("Table Created")

    except sqlite3.OperationalError:
        print("Table couldn't be Created")

#Import Naar Database
def add_to_database():
    """
    Functie voor het wegschrijven van variable naar de
    """
    db_conn.execute("INSERT INTO Fietsenstalling (Naam, Achternaam, Telefoon, FietsNr, PIN, otpKEY) VALUES "
                    "(?, ?, ?, ?, ?, ?);",(Naam, Achternaam, Adress, FietsNr, PIN,))

    db_conn.commit()

add_to_database()
print(print_database())
