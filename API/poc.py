from flask import Flask, request, jsonify
import json, os, subprocess

from flask_cors import CORS
app = Flask(__name__)
CORS(app)

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
    return json("pong")


@app.route('/start', methods=['GET'])
def start():
    subprocess.Popen(["python.exe", "API/poc_selenium.py", "token", "stream"])
    return jsonify(asnwer= "Process created")


@app.route('/info', methods=['GET'])
def info():
    stream = "stream"
    token = "token"
    return jsonify(readFile(stream, token))
    

app.run(host='0.0.0.0', port=4040)