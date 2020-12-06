import jwt, random, string

class MyJsonWebToken:

    secret = ''

    def __init__(self, secret=None):
        if secret is None or len(secret) == 0:
            self.secret = ''.join(random.choice(string.ascii_lowercase) for i in range(10))

    def create(self, username:str):
        token = jwt.encode({'username': username}, self.secret, algorithm='HS256')
        return token.decode("utf-8")
    
    def decode(self, token:str):
        try:
            return True, jwt.decode(token, self.secret, algorithms='HS256')['username']
        except Exception:
            return False, "Token invalid"