import psycopg2
from psycopg2 import pool
from configparser import ConfigParser

# Read config.ini file
config_object = ConfigParser()
config_object.read("config.ini")

# Get the creds
creds = config_object['creds']

connectionpool = pool.SimpleConnectionPool(
    1,
    5,
    database=creds['db'],
    user=creds['user'],
    password=creds['passwd']
    )

class ConnectionFromPool:
    def __init__(self):
        self.connection = None
    
    def __enter__(self):
        self.connection = connectionpool.getconn()
        return self.connection
    
    def __exit__(self):
        self.connection.commit()
        connectionpool.putconn(self.connection)
