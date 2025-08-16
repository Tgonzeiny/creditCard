import pytest
from backend.security.passwordHandler import PasswordHandler

def test_password_hashing():
    password = "testPassword123"

    # Hash the password
    hashed_password = PasswordHandler.hash_password(password)
    assert hashed_password is not None

    # Verify the password
    is_correct = PasswordHandler.check_password(hashed_password, password)
    assert is_correct == True

    # Test with an incorrect password
    is_incorrect = PasswordHandler.check_password(hashed_password, "wrongPassword")
    assert is_incorrect == False