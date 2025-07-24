import psycopg2
from backend.getDbConnection import getdbConnection

class UserCards:
    def __init__(self):
        self.conn = getdbConnection()
        self.cursor = self.conn.cursor()

    def addCardToUser(self, user_id, card_id, nickname=None):
        try:
            self.cursor.execute(
                """
                INSERT INTO user_cards (user_id, card_id, nickname)
                VALUES (%s, %s, %s)
                ON CONFLICT (user_id, card_id) DO NOTHING;
                """,
                (user_id, card_id, nickname)
            )
            self.conn.commit()
            return {"success": True, "message": "Card added to user"}
        except Exception as e:
            self.conn.rollback()
            return {"success": False, "message": str(e)}

    def getUserCards(self, user_id):
        self.cursor.execute(
            """
            SELECT uc.card_id, c.card_name, c.network, c.issuer, uc.nickname
            FROM user_cards uc
            JOIN credit_cards c ON uc.card_id = c.id
            WHERE uc.user_id = %s
            """,
            (user_id,)
        )
        return self.cursor.fetchall()

    def removeCardFromUser(self, user_id, card_id):
        self.cursor.execute(
            """
            DELETE FROM user_cards
            WHERE user_id = %s AND card_id = %s
            """,
            (user_id, card_id)
        )
        self.conn.commit()
        return {"success": True, "message": "Card removed"}

    def close(self):
        self.cursor.close()
        self.conn.close()
