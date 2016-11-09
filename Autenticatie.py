import sys
import random
sys.path.append('otpauth-master')
sys.path.append('six')
sys.path.append('python-qrcode-master')
from otpauth import OtpAuth

db_auth = 'B5F32F3EF4422334'
def nieuwe_gebruiker():
    global db_auth
    Random = str((''.join(random.choice('ABDJFHE34543234') for _ in range(16))))
    db_auth = Random
    print(Random)
    auth = OtpAuth(Random)  # Moet 16 lang zijn
    s = auth.to_uri('totp', 'Jelle Huisman', 'NS Fietsenstalling')
    import qrcode
    img = qrcode.make(s)
    img.show()

def controle_otp():
    auth = OtpAuth(db_auth)
    print(auth)
    controle = auth.valid_totp(int(input('Voer code in')))
    if controle == True:
         print('Code geaccepteerd')
    else:
         print('Helaas de code is onjuist')
nieuwe_gebruiker()
controle_otp()
