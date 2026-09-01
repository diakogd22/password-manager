# 🔐 Password Manager

A simple command-line Password Manager built with Python.

This project was created as a learning project to practice Python programming, file handling, encryption, password hashing, error handling, and project structure.

## ✨ Features

* 🔑 Master Password authentication
* 🔒 Password encryption using Fernet
* 🧂 Salted PBKDF2 password hashing
* ➕ Add passwords
* 👁️ View saved passwords
* 🔎 Search passwords
* ✏️ Edit passwords
* 🗑️ Delete passwords
* 🎲 Generate strong random passwords
* ⚠️ Basic error handling
* 📁 Organized multi-file project structure

## 🛠️ Technologies

* Python 3
* Cryptography
* Fernet symmetric encryption
* PBKDF2-HMAC
* Python `secrets` module

## 📂 Project Structure

```text
password-manager/
│
├── main.py
├── auth.py
├── crypto.py
├── password_manager.py
├── password_generator.py
│
├── data/
│   └── .gitkeep
│
├── .gitignore
├── requirements.txt
└── README.md
```

### File Overview

| File                    | Purpose                                       |
| ----------------------- | --------------------------------------------- |
| `main.py`               | Main application and user interface           |
| `auth.py`               | Master Password authentication                |
| `crypto.py`             | Password encryption and decryption            |
| `password_manager.py`   | Add, view, search, edit and delete operations |
| `password_generator.py` | Secure password generation                    |
| `requirements.txt`      | Project dependencies                          |
| `.gitignore`            | Prevents sensitive files from being committed |

## 🚀 Installation

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
cd password-manager
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python main.py
```

On the first run, the application will generate the encryption key and ask you to create a Master Password.

## 🔐 Security

Passwords stored by the application are encrypted using Fernet symmetric encryption.

The Master Password is not stored directly. A salted PBKDF2-HMAC hash is stored instead.

Sensitive local files are excluded from Git using `.gitignore`:

```text
data/key.key
data/master.hash
data/password.txt
```

## ⚠️ Disclaimer

This project is primarily intended for educational purposes.

It has not been audited for production-grade security and should not be used as the sole storage mechanism for highly sensitive real-world credentials.

## 📚 What I Learned

Through this project, I practiced:

* Python functions and modules
* File handling
* Exception handling
* Encryption and decryption
* Password hashing
* Salt generation
* Secure random password generation
* Working with virtual environments
* Project organization
* Git and GitHub workflow

## 📌 Future Improvements

Possible future features:

* Password strength checker
* Duplicate account detection
* Better terminal UI
* Clipboard support
* Automatic backups
* Database storage
* Unit tests
* More advanced authentication
* Improved error handling

## 👨‍💻 Author

Diako Goodarzi
