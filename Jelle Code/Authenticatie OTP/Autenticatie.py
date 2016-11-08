import sys
sys.path.append('otpauth-master')
sys.path.append('six')
sys.path.append('python-qrcode-master')
from otpauth import OtpAuth

auth = OtpAuth('JBSWY3DPEHPK3PXP')  # Moet 16 lang zijn
s = auth.to_uri('totp', 'Jelle Huisman', 'NS Fietsenstalling')
import qrcode
img = qrcode.make(s)
img.show()
controle = auth.valid_totp(int(input('Voer code in')))

if controle == True:
    print('Code geaccepteerd')
else:
    print('Helaas de code is onjuist')
