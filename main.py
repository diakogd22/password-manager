from auth import create_master_password, login
from password_manager import (
    add_password,
    view_passwords,
    search_password,
    delete_password,
    edit_password
)
from password_generator import generate_password
import os


def show_menu():
    print("\n")
    print("╔══════════════════════════════╗")
    print("║       PASSWORD MANAGER       ║")
    print("╠══════════════════════════════╣")
    print("║  1. Add Password             ║")
    print("║  2. View Passwords           ║")
    print("║  3. Search Password          ║")
    print("║  4. Delete Password          ║")
    print("║  5. Edit Password            ║")
    print("║  6. Generate Password        ║")
    print("║  7. Exit                     ║")
    print("╚══════════════════════════════╝")


def add():
    name = input("Account name: ").strip()

    if not name:
        print("Account name cannot be empty.")
        return

    if "|" in name:
        print("Account name cannot contain '|'.")
        return

    print("\n1. Enter password manually")
    print("2. Generate password")

    choice = input("Choose an option: ")

    if choice == "1":
        password = input("Password: ")

    elif choice == "2":
        try:
            length = int(input("Password length: "))

            if length < 8:
                print(
                    "Password length must be at least 8 characters."
                )
                return

            password = generate_password(length)

            print(f"\nGenerated password: {password}")

            confirm = input(
                "Use this password? (y/n): "
            ).lower()

            if confirm != "y":
                print("Password was not added.")
                return

        except ValueError:
            print("Please enter a valid number.")
            return

    else:
        print("Invalid option.")
        return

    try:
        add_password(name, password)
        print("Password added successfully!")

    except OSError:
        print("Error: Could not save password.")


def view():
    try:
        passwords = view_passwords()

        if not passwords:
            print("No passwords saved.")
            return

        for user, password in passwords:
            print(
                f"Account: {user} | Password: {password}"
            )

    except Exception as error:
        print(f"Error: {error}")


def search():
    name = input("Search account: ").strip()

    if not name:
        print("Search cannot be empty.")
        return

    try:
        password = search_password(name)

        if password is None:
            print("Account not found.")
        else:
            print(f"Account: {name}")
            print(f"Password: {password}")

    except Exception as error:
        print(f"Error: {error}")


def delete():
    name = input("Account to delete: ").strip()

    if not name:
        print("Account name cannot be empty.")
        return

    try:
        deleted = delete_password(name)

        if deleted:
            print("Account deleted successfully!")
        else:
            print("Account not found.")

    except Exception as error:
        print(f"Error: {error}")


def edit():
    name = input("Account to edit: ").strip()

    if not name:
        print("Account name cannot be empty.")
        return

    print("\n1. Enter password manually")
    print("2. Generate password")

    choice = input("Choose an option: ")

    if choice == "1":
        new_password = input("New password: ")

    elif choice == "2":
        try:
            length = int(input("Password length: "))

            if length < 8:
                print(
                    "Password length must be at least 8 characters."
                )
                return

            new_password = generate_password(length)

            print(
                f"\nGenerated password: {new_password}"
            )

            confirm = input(
                "Use this password? (y/n): "
            ).lower()

            if confirm != "y":
                print("Password was not changed.")
                return

        except ValueError:
            print("Please enter a valid number.")
            return

    else:
        print("Invalid option.")
        return

    try:
        updated = edit_password(
            name,
            new_password
        )

        if updated:
            print("Password updated successfully!")
        else:
            print("Account not found.")

    except Exception as error:
        print(f"Error: {error}")


def generate():
    try:
        length = int(input("Password length: "))

        if length < 8:
            print(
                "Password length must be at least 8 characters."
            )
            return

        password = generate_password(length)

        print(f"\nGenerated password: {password}")

    except ValueError:
        print("Please enter a valid number.")


def main():

    if not os.path.exists("data/master.hash"):
        print("No master password found.")

        if not create_master_password():
            return

    print("\n================================")
    print("       PASSWORD MANAGER")
    print("================================")

    try:
        if not login():
            print("Wrong master password!")
            return

    except (FileNotFoundError, OSError):
        print("Could not access master password.")
        return

    print("Login successful!")

    while True:

        show_menu()

        choice = input("Select an option: ")

        if choice == "1":
            add()

        elif choice == "2":
            view()

        elif choice == "3":
            search()

        elif choice == "4":
            delete()

        elif choice == "5":
            edit()

        elif choice == "6":
            generate()

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()