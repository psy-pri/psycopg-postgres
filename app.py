from database import Database
from user import User

Database.initialise() 
# print(Database.connection_pool.getconn())
my_user = User("chonklordferdinandmeows@gmail.com",'Chonklord','Ferdinand',None)

print(my_user)

my_user.save_to_db()

my_user = User.load_from_db_by_email('maxcatmeows@gmail.com')

print(my_user)



