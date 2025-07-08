import pytest
from backend.accountData.cards.cardDirectory import cardDirectory

#Checks if there is no card data in the database.
def test_getCards_none():
    request = cardDirectory()
    response = request.getAllCards()

    assert response == []
    request.close()

#Adds a dummy card and tests if it's in the database
def test_getCards():
    request = cardDirectory()
    add = request.addCard("AMEX Gold Card", "AMEX", "AMEX")
    assert add["success"] == True

    response = request.getAllCards()
    assert isinstance(response, list)

    # Check that at least one card has the expected name
    assert any(card["name"] == "AMEX Gold Card" for card in response)
    request.close()