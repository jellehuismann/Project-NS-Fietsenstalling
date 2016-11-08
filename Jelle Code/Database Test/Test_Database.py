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
def create_database():
    try:
        db_conn.execute('CREATE TABLE IF NOT EXISTS Fietsenstalling (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, '
                        'Naam TEXT ,Achternaam TEXT ,Adress TEXT ,Telefoon INTEGER ,FietsNr INTEGER ,PIN INTEGER ,otpKEY TEXT)')
        db_conn.commit()
        print("Table Created")

    except sqlite3.OperationalError:
        print("Table couldn't be Created")

#Import Naar Database
def add_to_database():
    db_conn.execute("INSERT INTO Fietsenstalling (Naam, Achternaam, Adress, FietsNr, PIN, otpKEY) VALUES "
                    "(?, ?, ?, ?, ?, ?);",(Naam, Achternaam, Adress, FietsNr, PIN, otpKEY))

    db_conn.commit()

add_to_database()

