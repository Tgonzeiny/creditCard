import mysql.connector


def getdbConnection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="test1234admin",
        database="creditcard"
    )