from user import User

my_user = User("glenncatmeows@gmail.com",'Glenn','Cat',None)

print(my_user)

my_user.save_to_db()

my_user = User.load_from_db_by_email('maxcatmeows@gmail.com')

print(my_user)

