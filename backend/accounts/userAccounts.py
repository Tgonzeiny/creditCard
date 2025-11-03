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

    def createUser(self, email, password):
        if self.userExists(email):
            return {"success": False, "message": "User already exists"}

        self.cursor.execute(
            "INSERT INTO users (email, password) VALUES (%s, %s)",
            (email, password)
        )
        self.conn.commit()
        return {"success": True, "message": "User created successfully"}

    def loginUser(self, email, password):
        self.cursor.execute(
            "SELECT * FROM users WHERE email = %s",
            (email,)
        )
        user = self.cursor.fetchone()
        if user:
            stored_hash = user[1]
            from backend.security.passwordHandler import PasswordHandler
            passwordHandler = PasswordHandler()
            if passwordHandler.check_password(stored_hash, password):
                return {"success": True, "message": "Login successful", "user_id": user[0]}
            else:
                return {"success": False, "message": "Invalid password"}
        else:
            return {"success": False, "message": "Invalid email or password"}
            
    def close(self):
        self.cursor.close()
        self.conn.close()

    def addCardToUser(self, user_id, card_id):
        try:
            self.cursor.execute("""
            INSERT INTO cards (user_id, card_id) 
            VALUES (%s, %s)
            ON CONFLICT DO NOTHING
            """, (user_id, card_id))

            return {"success": True, "message": "Card added successfully"}
        except Exception as e:
            print("Error adding card: ", e)
            return {"success": False, "message": "Failed to add card"}



