from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import os

app = Flask(__name__)
api = Api(app)

@app.route('/')
def running():
    return "Welcome to Dwellingly"

# #### ENDPOINT: USERS

# | method | route           | action                 |
# | :----- | :-------------- | :--------------------- |
# | POST   | `v1/users/`     | Creates a new user     |
# | GET    | `v1/users/`     | Gets all users         |
# | GET    | `v1/users/:uid` | Gets a single user     |
# | PATCH  | `v1/users/:uid` | Updates a single user  |
# | PUT    | `v1/users/:uid` | Archives a single user |
# | DELETE | `v1/users/:uid` | Deletes a single user  |

userList = [
    {
        "name": "Default User",
        "password": "userPassword",
        "username": "defaultUser",
        "email": "user1@dwellingly.com",
        "uid": "user0"
    },
    {
        "name": "Default User2",
        "password": "userPassword",
        "username": "defaultUser2",
        "email": "user2@dwellingly.com",
        "uid": "user1"
    }
]

# | GET    | `v1/users/`     | Gets all users  
@app.route('/v1/users/')
def get_users():
    return jsonify({"users": userList})

# | POST   | `v1/users/`     | Creates a new user  
@app.route('/v1/users', methods=["POST"])
def create_user():
    uid = "user" + str(len(userList))

    request_data = request.get_json()
    new_user = {
        "name": request_data["name"],
        "password": request_data["password"],
        "username": request_data["username"],
        "email": request_data["email"],
        "uid":uid
    }
    userList.append(new_user)
    return jsonify(new_user)

# | GET    | `v1/users/:uid` | Gets a single user   
@app.route('/v1/users/<string:uid>')
def get_user(uid):
    for user in userList:
        if user["uid"] == uid:
            return jsonify(user)
        
    return jsonify({"error": 301, "message": "User not found"})


# | PATCH  | `v1/users/:uid` | Updates a single user 
@app.route('/v1/users/<string:username>', methods=["PATCH"])
def update_user(uid):
    pass
    

# | DELETE | `v1/users/:uid` | Deletes a single user  |
@app.route('/v1/users/<string:uid>', methods=["DELETE"])
def delete_user(uid):
     pass



if __name__ == "__main__":
    app.run(host='0.0.0.0')
