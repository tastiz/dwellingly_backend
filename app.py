from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from api.security import authenticate, identity
from flask_sqlalchemy import SQLAlchemy

# from api.resources.users import Users


app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'super-secret'  # TODO: not this...
#app.secret_key = "1asdfha8dsfh3HUIE" #replace with .env keep it secret, keep it safe
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost/users'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

jwt = JWT(app, authenticate, identity)  # /auth token
#jwt will need to be implemented tested works with user class. will need to be tied to DB and put into
#Authorization header: JWT %HASH%

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True)
    email = db.Column(db.String(100), unique=True)

    def __init__(self, username, email ):
        self.username = username
        self.email = email 
    
    def __repr__(self):
        return '<User %r>' % self.username


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









