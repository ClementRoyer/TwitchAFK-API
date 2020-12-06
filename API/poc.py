from flask import Flask, request, jsonify
from flask_cors import CORS
from db import MyDB
import json, os, subprocess

app = Flask(__name__)
CORS(app)
db = MyDB('poc_db.json')

## Utils ##

def readFile(stream, token):
    try: 
        f = open("logs/" + token + "_" + stream + ".log")
        str = f.read()
        f.close()
        return str
    except Exception:
        return "Log couldn't be found."

## end utils

@app.route('/', methods=['GET'])
def home():
    return jsonify({'answer': 'pong'}), 200


# TODO : Redo, need to put body in param etc
@app.route('/create', methods=['GET'])
def createUser():
    user = {'username': 'jean', 'password': 'poc', 'token': 'poc'}
    db.addUser(user)
    return jsonify({'answer': 'success'}), 201


# @app.route('/connect', methods=['GET'])


# TODO : Redo this method, only made now to test, no even jsonify
@app.route('/token', methods=['GET'])
def getToken():
    return db.getUserToken('jean')


@app.route('/start', methods=['GET'])
def start():
    subprocess.Popen(["python.exe", "API/poc_selenium.py", "token", "stream"])
    return jsonify(answer= "Process created"), 200


@app.route('/info', methods=['GET'])
def info():
    stream = "stream"
    token = "token"
    return jsonify(readFile(stream, token)), 200
    

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4040)