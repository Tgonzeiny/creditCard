import pytest
from unittest.mock import MagicMock, patch
from backend.accounts.userCards import UserCards


@pytest.fixture
def mock_conn_cursor():
    with patch('backend.classes.userCards.getdbConnection') as mock_get_conn:
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_conn.cursor.return_value = mock_cursor
        mock_get_conn.return_value = mock_conn
        yield mock_conn, mock_cursor


def test_add_card_to_user_success(mock_conn_cursor):
    mock_conn, mock_cursor = mock_conn_cursor
    uc = UserCards()

    result = uc.addCardToUser(1, 2, "My Card")

    mock_cursor.execute.assert_called_once()
    mock_conn.commit.assert_called_once()
    assert result["success"] is True


def test_get_user_cards(mock_conn_cursor):
    mock_conn, mock_cursor = mock_conn_cursor
    uc = UserCards()

    mock_cursor.fetchall.return_value = [("1", "Chase Freedom", "Visa", "Chase", "Gas Card")]
    result = uc.getUserCards(1)

    mock_cursor.execute.assert_called_once()
    assert result == [("1", "Chase Freedom", "Visa", "Chase", "Gas Card")]


def test_remove_card_from_user(mock_conn_cursor):
    mock_conn, mock_cursor = mock_conn_cursor
    uc = UserCards()

    result = uc.removeCardFromUser(1, 2)

    mock_cursor.execute.assert_called_once()
    mock_conn.commit.assert_called_once()
    assert result["success"] is True


def test_add_card_duplicate_no_crash(mock_conn_cursor):
    mock_conn, mock_cursor = mock_conn_cursor
    uc = UserCards()

    # simulate unique constraint violation
    mock_cursor.execute.side_effect = Exception("duplicate key value violates unique constraint")
    result = uc.addCardToUser(1, 2, "My Card")

    mock_conn.rollback.assert_called_once()
    assert result["success"] is False
    assert "duplicate" in result["message"]
