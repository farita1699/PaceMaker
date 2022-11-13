from database.db import insert_users, list_users
def check_duplicate(inputUserName):
    users = list_users()
    for user in users:
        if (inputUserName == user[0]):
            return True
    return False
    
def check_exceed_max_users():
    users = list_users()
    if (len(users) >= 10): #Check if more than 10 users exist in db
        return True
    return False

def check_new_password(password):
    l, u, d, spacecount = 0, 0 ,0, 0
    capitalalphabets="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    smallalphabets="abcdefghijklmnopqrstuvwxyz"
    digits="0123456789"
    for i in password:
        # counting lowercase alphabets
        if (i in smallalphabets):
            l+=1           
        # counting uppercase alphabets
        if (i in capitalalphabets):
            u+=1           
        # counting digits
        if (i in digits):
            d+=1
        if (i == " "):
            spacecount+=1           
        # counting the mentioned special characters   
    if (l<1 or u<1 or d<1 or spacecount > 0 or len(password) < 8):
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
