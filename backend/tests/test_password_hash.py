import pytest
from backend.security.passwordHandler import PasswordHandler

def test_password_hashing():
    password = "testPassword123"
    handler = PasswordHandler()

    # Hash the password
    hashed_password = handler.hash_password(password)
    assert hashed_password is not None

    # Verify the password
    is_correct = handler.check_password(password, hashed_password)
    assert is_correct == True

    # Test with an incorrect password
    is_incorrect = handler.check_password("wrongPassword", hashed_password)
    assert is_incorrect == False