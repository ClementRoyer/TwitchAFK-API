from db import MyDB
from MyJWT import MyJsonWebToken


def readFile(stream, token):
    try: 
        f = open("logs/" + token + "_" + stream + ".log")
        str = f.read()
        f.close()
        return str
    except Exception:
        return "Log couldn't be found."


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