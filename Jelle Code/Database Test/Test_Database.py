import sqlite3
import sys
sys.path.append('otpauth-master')
sys.path.append('six')
sys.path.append('python-qrcode-master')
from otpauth import OtpAuth

connect = sqlite3.connect('database.db')
c = connect.cursor()

def create_table():
    try:
        c.execute('CREATE TABLE IF NOT EXISTS Fietsenstalling (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, '
              'Name TEXT, Adress TEXT, FietsNr INTEGER, PIN INTEGER, otpKEY TEXT)')
    except AttributeError:
        return 'Database is niet juist bijgewerkt controleer de database of controleer de code!'
#auth = OtpAuth('JBSWY3DPEHPK3PXP')  # a secret string
#auth.hotp()  # generate a count based code, default count is 4
#auth.valid_hotp(330810)
#auth.hotp(2)  # generate a count based code, count is 2
#auth.valid_hotp(720111)
#print(auth.totp())  # generate a time based code
#print(auth.valid_totp(157930))

auth = OtpAuth('JBSWY3DPEHPK3PXP')  # Moet 16 lang zijn
s = auth.to_uri('totp', 'Jelle Huisman', 'NS Fietsenstalling')
import qrcode
img = qrcode.make(s)
img.show()
controle = auth.valid_totp(int(input('Voer code in')))

print(controle)
print(create_table())

if controle == True:
    print('Code geaccepteerd')
else:
    print('Helaas de code is onjuist')
