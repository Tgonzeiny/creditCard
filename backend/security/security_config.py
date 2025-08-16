import os

BCRYPT_ROUNDS = int(os.getenv("BCRYPT_ROUNDS", 12))
PASSWORD_PEPPER = os.getenv("PASSWORD_PEPPER", "change_name_later")