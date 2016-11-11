import sys
import random
sys.path.append('otpauth-master')
sys.path.append('six')
sys.path.append('pymaging-master')
from otpauth import OtpAuth
from qrcode import *
db_auth = 0
auth = 0

def nieuwe_gebruiker():
    global db_auth
    Random = str((''.join(random.choice('ABDJFHE34543234') for _ in range(16))))
    db_auth = Random
    #print('test' + db_auth)
    auth = OtpAuth(Random)
    s = auth.to_uri('totp', 'NS', 'NS Fietsenstalling')
    qr = QRCode(version=1, error_correction=ERROR_CORRECT_L)
    qr.add_data(s)
    qr.make()
    img = qr.make_image()
    img.save("qrcode.png")
    return db_auth

def controle_otp(response, pincode):
    auth = OtpAuth(response)
    controle = auth.valid_totp(int(pincode))
    if controle == True:
         print('Code geaccepteerd')
         return True
    else:
         print('Helaas de code is onjuist')
         return False
#nieuwe_gebruiker()
#controle_otp('3324EH333D3DH3E3')
