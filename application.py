from flask import Flask, request
import hashlib

application = Flask(__name__)

memo = {}

@application.route('/')
def hello_world():
    return "Welcome!"

@application.route("/messages", methods=["POST"])
def post_message():
    message = request.json["message"]
    if not message:
        return "no message", 401

    hash_value = hashlib.sha256(message.encode('utf-8')).hexdigest()
    memo[hash_value] = message
    return hash_value, 200

@application.route("/messages", methods=["GET"])
def get_message():
    hash_value = request.args.get("hash")

    if hash_value in memo:
        return memo[hash_value], 200
    else:
        return "hash not found", 404

@application.route("/list")
def list_memo():
    return memo