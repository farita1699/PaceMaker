from database.db import insert_users, list_users
def check_duplicate(inputUserName):
    users = list_users()
    for user in users:
        if (inputUserName == user[0]):
            return True
    return False
def create_new_user(username, password):
    insert_users(username, password)
    print(list_users())

def login_check(inputUserName, inputPassword):
    users = list_users()
    for user in users:
        if (inputUserName == user[0] and inputPassword == user[1]):
            return True
    return False