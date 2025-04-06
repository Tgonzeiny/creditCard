import mysql.connector


def getdbConnection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Mitchdrools@2",
        database="creditcard"
    )