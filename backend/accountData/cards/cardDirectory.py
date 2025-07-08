#This class serves to get cards out of the "allCards" database containing card id number to card names

import psycopg2
from backend.config import DBConfig
from backend.getDbConnection import getdbConnection


class cardDirectory:
    def __init__(self):
        self.conn = getdbConnection()
        self.cursor = self.conn.cursor()

    #Gets a list of all cards to query from when adding a new card for your profile
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

    #Adds a new card to the database for the dev
    def addCard(self, name, network, issuer):

        if self.cardExists(name):
            return {"success": False, "message": "Card already exists"}

        self.cursor.execute(
            "INSERT INTO allCards (name, network, issuer) VALUES (%s, %s, %s)",
            (name, network, issuer)
        )
        self.conn.commit()
        return {"success": True, "message": "Card Added to Database"}

    #Checks if the card already exists in the database, I dont expect this to be used but will make handling requests much easier in the future
    def cardExists(self, name):

        self.cursor.execute("SELECT * FROM allCards WHERE name = %s", (name,))
        return self.cursor.fetchone() is not None

    def close(self):
        self.conn.close()
        self.cursor.clsoe()