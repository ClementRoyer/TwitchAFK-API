from db import MyDB
from MyJWT import MyJsonWebToken

import os, json


debug = False

def enableDebug():
    global debug
    debug = True

def readFile(stream, token):
    try: 
        f = open("logs/" + token + "_" + stream + ".log")
        str = f.read()
        f.close()
        return str
    except Exception:
        return "Log for " + token + "_" + stream + ".log" + " couldn't be found."


def writeInFile(f, obj):
    cout(obj)
    f.write(json.dumps(obj) + '\n')
    f.flush()


def writeTrunc(f, obj):
    cout(obj)
    f.truncate(0)
    f.write(json.dumps(obj))
    f.flush()


def validUser(user: dict):
    try :
        return user['username'] != None \
            and len(user['username']) != 0 \
            and user['password'] != None \
            and len(user['username']) != 0
    except Exception:
        return False
    return True


def tokenToUser(db : MyDB, jwt : MyJsonWebToken, token: str):
    ans, username = jwt.decode(token)
    if not ans:
        return ans, username # user = message of why it didn't work.
    user = db.getUser(username)
    if user is None:
        return False, "Token invalid." # user not found.
    return True, user

def cout(str):
    if debug:
        print(str)


def create_file(filename):
    cout("Creating file '" + filename + "'")
    return open(filename, "a")


def create_folder(folder):
    cout("Creating folder '" + folder + "'")
    if not os.path.exists(folder):
        os.mkdir(folder)