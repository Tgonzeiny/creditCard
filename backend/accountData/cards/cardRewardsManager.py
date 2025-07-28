#This class serves as a hook for adding new cards with mcc values

import psycopg2
from backend.config import DBConfig
from backend.getDbConnection import getdbConnection

class cardRewardsManager:
    def __init__(self):
        self.conn = getdbConnection()
        self.cursor = self.conn.cursor()


    def addReward(self, cardId, mccCategory, multiplier):
        try:
            self.cursor.execute(
                """
                INSERT INTO card_rewards (card_id, mcc_category, multiplier)
                VALUES (%s, %s, %s)
                ON CONFLICT DO NOTHING;
                """,
                (cardId, mccCategory.lower(), multiplier)
            )
            self.conn.commit()
            return {'success': True, 'message': 'Reward added successfully'}
        except Exception as e:
            self.conn.rollback()
            return {'success': False, 'message': str(e)}

    def getRewardsByCard(self, cardId):
        self.cursor.execute(
            "SELECT mcc_category, multiplier FROM card_rewards WHERE card_id = %s",
            (cardId,)
        )
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.conn.close()