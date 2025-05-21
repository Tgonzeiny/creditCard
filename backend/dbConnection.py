import mysql.connector

from backend.config import DBConfig

def getdbConnection():
    try:
        conn = mysql.connector.connect(**DBConfig)
        return conn
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
