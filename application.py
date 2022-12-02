from flask import Flask, request
import hashlib

application = Flask(__name__)

@application.route('/')
def hello_world():
    return 'Hello there good sir.'

@application.route("/messages", methods=["POST"])
def messages():
    message = request.json["message"]
    if not message:
        return "no message", 401

    hash_value = hashlib.sha256(message.encode('utf-8')).hexdigest()
    return hash_value, 200