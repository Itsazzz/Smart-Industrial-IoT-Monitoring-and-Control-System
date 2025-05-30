import mysql.connector
from Crypto.Cipher import AES
import base64

# -------- AES Utility Functions --------
BLOCK_SIZE = 16
key = b'mysecretkey12345'  # 16-byte key for AES-128

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

# -------- Connect to MySQL --------
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="cyberiot"
)
cursor = conn.cursor()

# -------- Create Table --------
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255),
    email TEXT
)
""")

# -------- Insert Encrypted Data --------
username = "john_doe"
plain_email = "john@example.com"
encrypted_email = encrypt(plain_email)

insert_query = "INSERT INTO users (username, email) VALUES (%s, %s)"
cursor.execute(insert_query, (username, encrypted_email))
conn.commit()

# -------- Read and Decrypt Data --------
cursor.execute("SELECT username, email FROM users")
rows = cursor.fetchall()

print("\nDecrypted Data from MySQL:")
for uname, enc_email in rows:
    decrypted_email = decrypt(enc_email)
    print(f"Username: {uname} | Email: {decrypted_email}")

# -------- Cleanup --------
cursor.close()
conn.close()
