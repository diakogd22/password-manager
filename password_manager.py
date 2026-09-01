from crypto import encrypt_password, decrypt_password


PASSWORD_FILE = "data/password.txt"


def add_password(name, password):
    encrypted_password = encrypt_password(password)

    with open(PASSWORD_FILE, "a") as file:
        file.write(
            f"{name}|{encrypted_password}\n"
        )


def view_passwords():
    passwords = []

    with open(PASSWORD_FILE, "r") as file:
        for line in file:
            data = line.strip()

            if not data:
                continue

            user, password = data.split("|", 1)

            decrypted_password = decrypt_password(
                password
            )

            passwords.append(
                (user, decrypted_password)
            )

    return passwords


def search_password(name):
    name = name.lower()

    with open(PASSWORD_FILE, "r") as file:
        for line in file:
            data = line.strip()

            if not data:
                continue

            user, password = data.split("|", 1)

            if user.lower() == name:
                return decrypt_password(password)

    return None


def delete_password(name):
    name = name.lower()
    found = False
    lines = []

    with open(PASSWORD_FILE, "r") as file:
        for line in file:
            data = line.strip()

            if not data:
                continue

            user, password = data.split("|", 1)

            if user.lower() == name:
                found = True
                continue

            lines.append(line)

    if found:
        with open(PASSWORD_FILE, "w") as file:
            file.writelines(lines)

    return found


def edit_password(name, new_password):
    name = name.lower()
    found = False
    lines = []

    with open(PASSWORD_FILE, "r") as file:
        for line in file:
            data = line.strip()

            if not data:
                continue

            user, password = data.split("|", 1)

            if user.lower() == name:
                encrypted_password = encrypt_password(
                    new_password
                )

                lines.append(
                    f"{user}|{encrypted_password}\n"
                )

                found = True

            else:
                lines.append(line)

    if found:
        with open(PASSWORD_FILE, "w") as file:
            file.writelines(lines)

    return found