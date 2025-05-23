#This class will handle all account based interactions with the database.

import mysql.connector
from backend.config import DBConfig

class userAccounts:

    def __init__(self):
        self.conn = mysql.connector.connect(**DBConfig)
        self.cursor = self.conn.cursor(dictionary=True)

    #Checks if email exists in the users database and returns True if it does
    def userExists(self, email):
        self.cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        return self.cursor.fetchone() is not None

    def createUser(self, username, password, email):
        if self.userExists(email):
            return {"success": False, "message": "User already exits"}

        self.cursor.execute(
            "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)",
            (username, email, password)
        )
        self.conn.commit()
        return {"success": True, "message": "User created successfully"}

    def close(self):
        self.cursor.close()
        self.conn.close()


