from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import os

app = Flask(__name__)
api = Api(app)

@app.route('/')
def running():
    return "Up and Running"


if __name__ == "__main__":
    app.run(host='0.0.0.0')
