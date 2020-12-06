from flask import Flask, request, jsonify
from flask_cors import CORS

from db import MyDB
from utils import readFile, validUser, tokenToUser
from MyJWT import MyJsonWebToken

import json, os, subprocess, signal, atexit


DEBUG = True

app = Flask(__name__)
CORS(app)
db = MyDB('api_db.json')
jwt = MyJsonWebToken()

@app.route('/', methods=['GET'])
def home():
    return jsonify({'answer': 'pong'}), 200


@app.route('/create', methods=['post'])
def createUser():
    user = request.json
    if not validUser(user):
        return jsonify({'answer': 'failure', 'toast': 'Input form invalid.'}), 400
    ans = db.addUser(user)
    if ans is not None:
        return jsonify({'answer': 'failure', 'toast': ans}), 400
    return jsonify({'answer': 'success'}), 201


@app.route('/connect', methods=['post'])
def connect():
    user = request.json
    if not validUser(user):
        return jsonify({'answer': 'failure', 'toast': 'Input form invalid.'}), 400
    ans = db.getUser(user['username'])
    if ans is None or ans['password'] != user['password']:
        return jsonify({'answer': 'failure', 'toast': 'User/password not found.'}), 400
    return jsonify({'answer': 'success', 'token': jwt.create(user['username']), 'toast': 'Login success'}), 200


@app.route('/delete', methods=['post'])
def delAccount():
    token = request.headers.get('Authorization')
    ans, user = tokenToUser(db, jwt, token)
    if not ans:
        return jsonify({'answer': 'failure', 'toast': user}), 400
    db.deleteUser(user['username'])
    return jsonify({'answer': 'success', 'toast': 'User deleted'}), 200
    


# TODO : Redo this method, only made now to test, no even jsonify
@app.route('/token', methods=['GET'])
def getToken():
    return db.getUserToken('jean')

w
@app.route('/start', methods=['GET'])
def start():
    subprocess.Popen(["python.exe", "API/poc_selenium.py", "token", "stream"])
    return jsonify(answer= "Process created"), 200


@app.route('/info', methods=['GET'])
def info():
    stream = "stream"
    token = "token"
    return jsonify(readFile(stream, token)), 200
    



def signal_handler(sig, frame):
    end()


def end():
    global DEBUG
    print("API ENDING")
    try:
        db.end(delete = DEBUG)
    except Exception:
        pass




if __name__ == "__main__":
    try:
        app.run(host='0.0.0.0', port=4040)
    except KeyboardInterrupt:
        end()


signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGSEGV, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)
atexit.register(end)