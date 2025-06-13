import hashlib, json, os
from utils.encryptor import encrypt_data, decrypt_data

DB_FILE = "data/database.json"

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register(username, password, role):
    users = load_users()
    if username in users:
        return "User already exists"
    users[username] = {
        "password": hash_password(password),
        "role": role
    }
    save_users(users)
    return "User registered successfully"

def login(username, password):
    users = load_users()
    if username in users and users[username]["password"] == hash_password(password):
        return users[username]["role"]
    return None

def load_users():
    if not os.path.exists(DB_FILE):
        return {}
    with open(DB_FILE, "rb") as f:
        return json.loads(decrypt_data(f.read()))

def save_users(users):
    with open(DB_FILE, "wb") as f:
        f.write(encrypt_data(json.dumps(users)))

def get_users():
    users = load_users()
    return [f"{u} ({v['role']})" for u, v in users.items()]