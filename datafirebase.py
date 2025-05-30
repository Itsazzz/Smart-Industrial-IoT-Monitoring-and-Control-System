from firebase import firebase
import time
import mysql.connector
from Crypto.Cipher import AES
import base64

# -------- AES Utility Functions --------
BLOCK_SIZE = 16
key = b'aab12fye2312345y'  # 16-byte key for AES-128

def pad(s):
    pad_len = BLOCK_SIZE - len(s.encode('utf-8')) % BLOCK_SIZE
    return s + (chr(pad_len) * pad_len)

def unpad(s):
    return s[:-ord(s[-1:])]

def encrypt(raw_text):
    raw_padded = pad(raw_text)
    cipher = AES.new(key, AES.MODE_ECB)
    encrypted_bytes = cipher.encrypt(raw_padded.encode('utf-8'))
    return base64.b64encode(encrypted_bytes).decode('utf-8')

def decrypt(enc_text):
    cipher = AES.new(key, AES.MODE_ECB)
    decoded = base64.b64decode(enc_text)
    decrypted = cipher.decrypt(decoded).decode('utf-8')
    return unpad(decrypted)

# Initialize Firebase
firebase = firebase.FirebaseApplication('https://esp32blockchaindata-default-rtdb.firebaseio.com/', None)
from datetime import datetime, date, timedelta
now = datetime.now()
date = formatted = now.strftime("%Y-%m-%d")
def read_firebase():
    # Read data from /sensor/dht
    result = firebase.get('/ESP321', None)

    print("Data from Firebase:")
    print(result)

    # Access individual values
    if result:
        hum = result.get('humidity')
        status = result.get('relay_state')
        temp = result.get('temperature')
        hum1 = encrypt(str(hum))
        temp1 = encrypt(str(temp))
        #hum = encrypt(hum)




        conn = mysql.connector.connect(user='root', password='', host='localhost', database='cyberiot1')
        cursor = conn.cursor()
        cursor.execute(
            "update iotdata set date='" + str(date) + "',envi_humidity='" + str(hum1) + "',load_temperature='" + str(temp1) + "',status='" + str(status) + "' where id='1'")
        conn.commit()
        conn.close()
def read_firebase1():
    # Read data from /sensor/dht
    result = firebase.get('/ESP322', None)

    print("Data from Firebase:")
    print(result)

    # Access individual values
    if result:
        hum = result.get('humidity')
        status = result.get('relay_state')
        temp = result.get('temperature')
        hum1 = encrypt(str(hum))
        temp1 = encrypt(str(temp))




        conn = mysql.connector.connect(user='root', password='', host='localhost', database='cyberiot1')
        cursor = conn.cursor()
        cursor.execute(
            "update iotdata1 set date='" + str(date) + "',envi_humidity='" + str(hum1) + "',load_temperature='" + str(
                temp1) + "',status='" + str(status) + "' where id='1'")
        conn.commit()
        conn.close()



while True:
    read_firebase()
    read_firebase1()

    time.sleep(5)
