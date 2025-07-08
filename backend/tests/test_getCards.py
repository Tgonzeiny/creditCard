import pytest
from backend.accountData.cards.cardDirectory import cardDirectory

#Checks if there is no card dat in the database.
def test_getCards_none():
    request = cardDirectory()
    response = request.getAllCards()

    assert response is None
    request.close()

#Adds a dummy card and tests if it's in the database
def test_getCards():
    request = cardDirectory()
    add = request.addCard("AMEX Gold Card", "Visa", "AMEX")
    response = request.getAllCards()
    assert response is not None
    request.close()