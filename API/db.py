from tinydb import TinyDB, Query, Storage

import os

class MyDB:
    __dbFile : str
    __db : TinyDB
    __userTable = ''
    __watchTable = ''

    def __init__(self, dbfile: str):
        if len(dbfile) == 0:
            dbfile = '.db.json'
        self.__dbFile = dbfile
        self.__db = TinyDB(dbfile)
        self.__userTable = self.__db.table("user")
        self.__watchTable = self.__db.table("watch")


    # User

    def userExist(self, name):
        try :
            q = Query()
            return len(self.__userTable.search(q.username == name)) > 0
        except Exception:
            return False


    def getUserToken(self, name):
        if not self.userExist(name):
            return None
        try : 
            q = Query()
            return self.__userTable.search(q.username == name)[0]['token']
        except Exception:
            return None


    def setUserToken(self, name, token):
        if not self.userExist(name):
            return False
        try:
            q = Query()
            self.__userTable.update({'token': token}, q.username == name)
        except Exception:
            return False
        return True


    def getUser(self, name):
        try :
            q = Query()
            return self.__userTable.get(q.username == name)
        except Exception:
            return None


    def addUser(self, user: dict):
        if not self.userExist(user['username']):
            self.__userTable.insert(user)
            return None
        return 'User already exist.'


    def deleteUser(self, username: str):
        if not self.userExist(username):
            return False
        try:
            q = Query()
            self.__watchTable.remove(q.username == username)
            self.__userTable.remove(q.username == username)
        except Exception:
            return False
        return True


    # watcher

    def watcherExist(self, username: str, stream: str):
        try :
            q = Query()
            return self.__watchTable.get((q.username == username) 
                                        & (q.stream == stream)) is not None
        except Exception:
            return False
        return True


    def getAllByUser(self, username: str):
        if not self.userExist(username):
            return False
        q = Query()
        return self.__watchTable.search(q.username == username)


    def addWatcher(self, username: str, stream: str):
        if not self.userExist(username) or self.watcherExist(username, stream):
            return False
        self.__watchTable.insert({'username': username, 'stream': stream})
        return True

    
    def getWatcher(self, name: str, stream: str):
        try :
            q = Query()
            return self.__watchTable.get((q.username == name) 
                                        & (q.stream == stream))
        except Exception:
            return None


    def deleteWatcher(self, username: str, stream: str):
        if not self.watcherExist(username, stream):
            return False
        q = Query()
        self.__watchTable.remove((q.username == username) & (q.stream == stream))
        return True


    ## Utils

    def end(self, delete=False):
        self.__db.storage.close()
        if delete:
            os.remove(self.__dbFile)
    

def test_user(db: MyDB):
    assert db.userExist('junit') == False
    assert db.addUser({'username': 'junit', 'password': 'key', 'token' : 'tok'}) == None
    assert db.userExist('junit') == True
    assert db.getUser('junit') != None
    assert db.setUserToken('junit', 'new token') == True
    assert db.getUserToken('junit') == 'new token'
    assert db.addUser({'username': 'junit', 'password': 'key', 'token' : 'tok'}) == 'User already exist.'
    assert db.deleteUser('junit') == True
    assert db.userExist('junit') == False


def test_watcher(db: MyDB):
    db.addUser({'username': 'junit', 'password': 'key', 'token' : 'tok'})
    assert db.watcherExist('junit', 'solary') == False
    assert db.addWatcher('junit', 'solary') == True
    assert db.addWatcher('junit', 'kamet0') == True
    assert len(db.getAllByUser('junit')) == 2
    assert db.watcherExist('junit', 'solary') == True
    assert db.deleteWatcher('junit', 'solary') == True
    assert db.watcherExist('junit', 'solary') == False
    assert db.deleteUser('junit') == True

def test():
    db = MyDB('.tinydb.json')
    test_user(db)
    test_watcher(db)
    print('Test : success')
    db.end(delete = True)


if __name__ == "__main__":
    test()
