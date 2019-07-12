from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from security import authenticate, identity


app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'super-secret'  # TODO: not this...
#app.secret_key = "1asdfha8dsfh3HUIE" #replace with .env keep it secret, keep it safe
api = Api(app)


jwt = JWT(app, authenticate, identity)  # /auth token
#jwt will need to be implemented tested works with user class. will need to be tied to DB and put into
#Authorization header: JWT %HASH%





userList = [
    {
        "name": "Default User",
        "password": "userPassword",
        "username": "defaultUser",
        "email": "user1@dwellingly.com",
        "archived": "false",
        "id": "user0"
    },
    {
        "name": "Default User2",
        "password": "userPassword",
        "username": "defaultUser2",
        "email": "user2@dwellingly.com",
        "archived": "false",
        "id": "user1"
    }
]









