#This class serves to get cards out of the "allCards" database containing card id number to card names

import psycopg2
from backend.config import DBConfig
from backend.getDbConnection import getdbConnection


class cardDirectory:
    def __init__(self):
        self.conn = getdbConnection()
        self.cursor = self.conn.cursor()

    def getAllCards(self):
        self.cursor.execute("SELECT id, name, network, issuer FROM allCards ORDER BY namne ASC;")
        rows = self.cursor.fetchall()

        return [
            {
                "id": row[0],
                "name": row[1],
                "network": row[2],
                "issuer": row[3]
            } for row in rows
        ]

    def close(self):
        self.conn.close()
        self.cursor.clsoe()