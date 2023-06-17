import os
import bcrypt

salt = os.getenv("PASSWORD_SALT").encode()

def encrypt_password(password: str):
    hashed_password = bcrypt.hashpw(password.encode(), salt)
    return hashed_password.decode()