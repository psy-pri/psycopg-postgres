from database import Database
from database import creds
from user import User
from new_user import email,first_name,last_name

Database.initialise(database=creds['db'],user=creds['user'],password=creds['passwd']) 
# print(Database.connection_pool.getconn())
my_user = User(email,first_name,last_name,None)

print(my_user)

my_user.save_to_db()

my_user = User.load_from_db_by_email(email)

print(my_user)



