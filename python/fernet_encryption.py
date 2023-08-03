import os

from cryptography.fernet import Fernet

FERNET_KEY = os.environ["FERNET_KEY"]


def encrypt_message(message):
    f = Fernet(FERNET_KEY.encode())
    return f.encrypt(message.encode()).decode()


def decrypt_message(encrypted_message):
    f = Fernet(FERNET_KEY.encode())
    return f.decrypt(encrypted_message.encode()).decode()
