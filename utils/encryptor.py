from cryptography.fernet import Fernet
import os

KEY_FILE = "data/secret.key"

if os.path.exists(KEY_FILE):
    with open(KEY_FILE, "rb") as kf:
        key = kf.read()
else:
    key = Fernet.generate_key()
    os.makedirs("data", exist_ok=True)
    with open(KEY_FILE, "wb") as kf:
        kf.write(key)

fernet = Fernet(key)

def encrypt_data(data):
    return fernet.encrypt(data.encode())

def decrypt_data(data):
    return fernet.decrypt(data).decode()