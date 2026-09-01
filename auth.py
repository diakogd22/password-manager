import hashlib
import getpass
import os
import secrets


MASTER_FILE = "data/master.hash"

def hash_password(password, salt):
    return hashlib.pbkdf2_hmac(
        "sha256",
        password.encode(),
        salt,
        200_000
    )


def create_master_password():
    password = getpass.getpass("Create master password: ")
    confirm = getpass.getpass("Confirm master password: ")

    if password != confirm:
        print("Passwords do not match.")
        return False

    if len(password) < 8:
        print("Master password must be at least 8 characters.")
        return False

    salt = secrets.token_bytes(16)

    password_hash = hash_password(password, salt)

    with open(MASTER_FILE, "wb") as file:
        file.write(salt + password_hash)

    print("Master password created successfully.")
    return True


def login():
    password = getpass.getpass("Enter master password: ")

    with open(MASTER_FILE, "rb") as file:
        data = file.read()

    salt = data[:16]
    stored_hash = data[16:]

    password_hash = hash_password(
        password,
        salt
    )

    return secrets.compare_digest(
        password_hash,
        stored_hash
    )