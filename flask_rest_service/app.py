import json
from flask import Flask, request, jsonify, abort

app = Flask(__name__)


@app.route("/")
def index():
    return jsonify({"status":"success"})


@app.route("/numbers", methods=["GET"])
def getName():
    return jsonify({"numbers": list(range(5)), "method":"GET"})

app.run(host='0.0.0.0', port=5100)
