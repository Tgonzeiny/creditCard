import psycopg2
from backend.config import DBConfig


def getdbConnection():
    try:
        conn = psycopg2.connect(**DBConfig)
        return conn
    except Exception as e:
        print(f"PostgreSQL Connecction Error: {e}")
        return None
