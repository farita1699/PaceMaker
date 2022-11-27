from database.db import insert_users, list_users, list_parameters
import config

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

def check_new_password(password): #Check for improvements using Regex
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

def check_new_username(username):
    #Make sure no spaces, and username cannot be empty
    spacecount = 0
    for i in username: 
        if (i == " "):
            spacecount += 1
    if (spacecount > 0) or len(username) <= 0:
        return True
    return False


def create_new_user(username, password):
    insert_users(username, password)
    print(list_users())
    print(list_parameters())

def login_check(inputUserName, inputPassword):#This functio
    users = list_users()
    for user in users:
        if (inputUserName == user[0] and inputPassword == user[1]):
            return user[2]
    return 0

def get_user_info(id, username):
    allAOOParameters = list_parameters('AOO')
    allVOOParameters = list_parameters('VOO')
    allAAIParameters = list_parameters('AAI')
    allVVIParameters = list_parameters('VVI')
    if (len(allAOOParameters) != len(allVOOParameters) or len(allVOOParameters) != len(allAAIParameters) or len(allAAIParameters) != len(allVVIParameters)):
        return False

    for i in range(len(allAOOParameters)):
        if (allAOOParameters[i][4] == id and allVOOParameters[i][4] == id and allAAIParameters[i][6] == id and allVVIParameters[i][6] == id):
            config.cache['AOO'] = {
                'LRL': allAOOParameters[i][0],
                'URL': allAOOParameters[i][1],
                'APW': allAOOParameters[i][2],
                'AA': allAOOParameters[i][3]
                }
            config.cache['VOO'] = {
                'LRL': allVOOParameters[i][0],
                'URL': allVOOParameters[i][1],
                'VPW': allVOOParameters[i][2],
                'VA': allVOOParameters[i][3]
                }
            config.cache['AAI'] = {
                'LRL': allAAIParameters[i][0],
                'URL': allAAIParameters[i][1],
                'APW': allAAIParameters[i][2],
                'AA': allAAIParameters[i][3],
                'AT': allAAIParameters[i][4],
                'RP': allAAIParameters[i][5],
                }
            config.cache['VVI'] = {
                'LRL': allVVIParameters[i][0],
                'URL': allVVIParameters[i][1],
                'VPW': allVVIParameters[i][2],
                'VA': allVVIParameters[i][3],
                'VT': allVVIParameters[i][4],
                'RP': allVVIParameters[i][5],
                }
    config.cache['id'] = id
    print(config.cache)
    return True
    
