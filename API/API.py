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

process = ({})

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


@app.route('/delete', methods=['DELETE'])
def delAccount():
    token = request.headers.get('Authorization')
    ans, user = tokenToUser(db, jwt, token)
    if not ans:
        return jsonify({'answer': 'failure', 'toast': user}), 400
    db.deleteUser(user['username'])
    return jsonify({'answer': 'success', 'toast': 'User deleted'}), 200
    

@app.route('/token', methods=['PUT'])
def setToken():
    token = request.headers.get('Authorization')
    twitch_token = request.json['token']
    ans, user = tokenToUser(db, jwt, token)
    if not ans:
        return jsonify({'answer': 'failure', 'toast': user}), 400
    if not db.setUserToken(user['username'], twitch_token):
        return jsonify({'answer': 'failure', 'toast': 'Impossible'}), 400
    return jsonify({'answer': 'success', 'toast': 'token updated'})


@app.route('/start', methods=['POST'])
def start():
    global process
    token = request.headers.get('Authorization')
    stream = request.args['stream']
    if stream is None or len(stream) == 0:
        return jsonify({'answer': 'failure', 'toast': 'stream name missing.'}), 400
    ans, user = tokenToUser(db, jwt, token)
    if not ans:
        return jsonify({'answer': 'failure', 'toast': user}), 400
    if not db.addWatcher(user['username'], stream):
        return jsonify({'answer': 'failure', 'toast': 'Already watching this stream.'}), 400
    watcher = db.getWatcher(user['username'], stream)
    process[watcher.doc_id] = subprocess.Popen(["python.exe", "API/poc_selenium.py", user['username'], stream])
    return jsonify(answer= "Process created"), 200


@app.route('/stop', methods=['POST'])
def stop():
    global process
    token = request.headers.get('Authorization')
    stream = request.args['stream']
    if stream is None or len(stream) == 0:
        return jsonify({'answer': 'failure', 'toast': 'stream name missing.'}), 400
    ans, user = tokenToUser(db, jwt, token)
    if not ans:
        return jsonify({'answer': 'failure', 'toast': user}), 400
    if not db.watcherExist(user['username'], stream):
        return jsonify({'answer': 'failure', 'toast': 'Impossible.'}), 400
    watcher = db.getWatcher(user['username'], stream)
    process[watcher.doc_id].kill()
    db.deleteWatcher(user['username'], stream)
    return jsonify({'answer': 'success', 'toast': 'Process stopped'}), 200


@app.route('/watchers', methods=['GET'])
def watchers():
    token = request.headers.get('Authorization')
    ans, user = tokenToUser(db, jwt, token)
    if not ans:
        return jsonify({'answer': 'failure', 'toast': user}), 400
    l = db.getAllByUser(user['username'])
    return jsonify(answer='success', object=l), 200


@app.route('/info', methods=['GET'])
def info():
    token = request.headers.get('Authorization')
    stream = request.args['stream']
    if stream is None or len(stream) == 0:
        return jsonify({'answer': 'failure', 'toast': 'stream name missing.'}), 400
    ans, user = tokenToUser(db, jwt, token)
    if not ans:
        return jsonify({'answer': 'failure', 'toast': user})
    return jsonify(answer='success', log=readFile(stream, user['username'])), 200


@app.route('/logs', methods=['GET'])
def alllogs():
    token = request.headers.get('Authorization')
    stream = request.args['stream']
    if stream is None or len(stream) == 0:
        return jsonify({'answer': 'failure', 'toast': 'stream name missing.'}), 400
    ans, user = tokenToUser(db, jwt, token)
    if not ans:
        return jsonify({'answer': 'failure', 'toast': user})
    return jsonify(answer='success', logs=readFile(stream+'_long', user['username'])), 200


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