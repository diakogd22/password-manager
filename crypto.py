from cryptography.fernet import Fernet
import os


KEY_FILE = "data/key.key"


def load_key():
    if not os.path.exists(KEY_FILE):
        os.makedirs("data", exist_ok=True)

        key = Fernet.generate_key()

        with open(KEY_FILE, "wb") as file:
            file.write(key)

        return key

    with open(KEY_FILE, "rb") as file:
        return file.read()


key = load_key()
fer = Fernet(key)


def encrypt_password(password):
    return fer.encrypt(
        password.encode()
    ).decode()


def decrypt_password(password):
    return fer.decrypt(
        password.encode()
    ).decode()