import sys
import random
sys.path.append('otpauth-master')
sys.path.append('six')
sys.path.append('pymaging-master')
from otpauth import OtpAuth
from qrcode import *
db_auth = 0

def nieuwe_gebruiker():
    global db_auth
    Random = str((''.join(random.choice('ABDJFHE34543234') for _ in range(16))))
    db_auth = Random
    db_auth2= db_auth
    print(db_auth)
    print(db_auth2)
    auth = OtpAuth(Random)
    s = auth.to_uri('totp', 'NS', 'NS Fietsenstalling')
    qr = QRCode(version=1, error_correction=ERROR_CORRECT_L)
    qr.add_data(s)
    qr.make()
    img = qr.make_image()
    img.save("qrcode.png")

def controle_otp(response):
    auth = OtpAuth(response)
    controle = auth.valid_totp(int(input('Voer code in')))
    if controle == True:
         print('Code geaccepteerd')
    else:
         print('Helaas de code is onjuist')
nieuwe_gebruiker()
