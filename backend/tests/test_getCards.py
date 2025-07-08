import pytest
from backend.accountData.cards.cardDirectory import cardDirectory

def test_getCards():
    request = cardDirectory()
    respone =