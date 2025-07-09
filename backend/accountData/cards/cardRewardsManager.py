#This class serves as a hook for adding new cards with mcc values

import psycopg2
from backend.config import DBConfig
from backend.getDbConnection import getdbConnection

class cardRewardsManager:
    def __init__(self):
        self.conn = getdbConnection()
        self.cursor = self.conn.cursor()


