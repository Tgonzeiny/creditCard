import pytest
from backend.accounts.userAccounts import userAccounts

#Tests if an user can be made
def testCreateUser():
    user = userAccounts()
    response = user.createUser("TestUser", "test@example.com", "test123")
    assert response["success"] is True or response["message"] == "User created successfully"
    user.close()

#Tests if user can be made if email exits
def testDCreateDuplicateUser():
    user = userAccounts()
    user.createUser("TestUser", "test@example.com", "test123")
    result = user.createUser("TestUser", "test@example.com", "test123")
    assert result["success"] is False
    assert result["message"] == "User already exists"
    user.close()