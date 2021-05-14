from database import CursorFromConnectionFromPool

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
        with CursorFromConnectionFromPool() as cursor:
            cursor.execute('INSERT INTO psy.users (email,first_name,last_name) VALUES (%s,%s,%s)',(self.email,self.first_name,self.last_name))
    
    @classmethod
    def load_from_db_by_email(cls,email):
        with CursorFromConnectionFromPool() as cursor:
            cursor.execute('SELECT * FROM psy.users where email = %s',(email,))
            user_data = cursor.fetchone()
            return cls(email = user_data[0], first_name = user_data[1], last_name = user_data[2], id = user_data[3])
