import bcrypt
from .security_config import BCRYPT_ROUNDS, PASSWORD_PEPPER
#Built to handle password hashing and verification using bcrypt.

class PasswordHandler:
    @staticmethod
    def hash_password(password):
        hashed = bcrypt.hashpw((password + PASSWORD_PEPPER).encode('utf-8'), bcrypt.gensalt(rounds=BCRYPT_ROUNDS))
        return hashed.decode('utf-8')

    @staticmethod
    def check_password(hashed: str, password: str) -> bool:
        """Checks a password against a hashed password."""
        return bcrypt.checkpw((password+PASSWORD_PEPPER).encode('utf-8'), hashed.encode('utf-8'))