from flask import Flask, request
import hashlib

application = Flask(__name__)

@application.route('/')
def hello_world():
    return "Welcome!"

@application.route("/messages", methods=["POST"])
def messages(): # TODO: post_message
    message = request.json["message"]
    if not message:
        return "no message", 401

    hash_value = hashlib.sha256(message.encode('utf-8')).hexdigest()
    return hash_value, 200

@application.route("/messages", methods=["GET"])
def get_message():
    hash_value = request.args.get("hash")

    if hash_value == "6e8c90bed1ab401092001331be8803c89c5ca2d0283b7d8cbbb5dc19bf483cef": #TODO: change it
        return "feyza", 200 #TODO: change it
    else:
        return "hash not found", 404