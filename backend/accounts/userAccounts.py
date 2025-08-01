#This class will handle all account based interactions with the database.

import psycopg2
from backend.config import DBConfig

class userAccounts:

    def __init__(self):
        self.conn = psycopg2.connect(**DBConfig)
        self.cursor = self.conn.cursor()

    #Checks if email exists in the users database and returns True if it does
    def userExists(self, email):
        self.cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        return self.cursor.fetchone() is not None

    def createUser(self, username, email, password):
        if self.userExists(email):
            return {"success": False, "message": "User already exists"}

        self.cursor.execute(
            "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)",
            (username, email, password)
        )
        self.conn.commit()
        return {"success": True, "message": "User created successfully"}

    def loginUser(self, email, password):
        self.cursor.execute(
            "SELECT * FROM users WHERE email = %s AND password = %s",
            (email, password)
        )
        user = self.cursor.fetchone()
        if user:
            return {"success": True, "message": "Login successful", "user_id": user[0]}
        else:
            return {"success": False, "message": "Invalid username or password"}
            
    def close(self):
        self.cursor.close()
        self.conn.close()


