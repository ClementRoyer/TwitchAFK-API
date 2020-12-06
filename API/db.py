from tinydb import TinyDB, Query

class MyDB:
    db : TinyDB
    
    def __init__(self, dbfile: str):
        if len(dbfile) == 0:
            dbfile = '.db.json'
        self.db = TinyDB(dbfile)


    def userExist(self, name):
        try :
            q = Query()
            return len(self.db.search(q.username == name)) > 0
        except Exception:
            return False


    def getUserToken(self, name):
        if not self.userExist(name):
            return '-1'
        try : 
            q = Query()
            return self.db.search(q.username == name)[0]['token']
        except Exception:
            return '-1'


    def addUser(self, user: dict):
        if not self.userExist(user['username']):
            self.db.insert(user)
            return True
        return False


if __name__ == "__main__":
    db = MyDB('.tinydb.json')
    print(db.addUser({'username': 'poc', 'password': 'key', 'token' : 'tok'}))
    print(db.addUser({'username': 'poc', 'password': 'key', 'token' : 'tok'}))
    print(db.getUserToken('poc'))
    print(db.getUserToken('none'))
