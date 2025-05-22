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

    def createUser(selfself, username, ):

