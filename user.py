import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()

class User:
    def __init__(self, email, first_name, last_name, id):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.id = id

    def __repr__(self):
        return "<User details: {} {} {}>".format(self.email,self.first_name,self.last_name)

    def save_to_db(self):
        #establish db connection
        connection = psycopg2.connect(database = os.getenv("db"), user = "postgres", password = "priyanka123", 
        host = os.getenv("host"))
        #open cursor
        with connection.cursor() as cursor:
            #execute sql queries
            cursor.execute('INSERT INTO psy.users VALUES (%s,%s,%s)',(self.email,self.first_name,self.last_name))
        #commit changes
        connection.commit()
        #close cursor
        connection.close()