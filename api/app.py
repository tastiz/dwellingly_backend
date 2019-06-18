from flask import Flask, jsonify, request
from flask_restful import Resource, Api,reqparse
from flask_jwt import JWT, jwt_required
from security import authenticate, identity


app = Flask(__name__)
app.secret_key = "1asdfha8dsfh3HUIE" #replace with .env keep it secret, keep it safe
api = Api(app)

# jwt = JWT(app, authenticate, identity ) # /auth token 
# jwt will need to be implemented tested works with user class. will need to be tied to DB and put into 
#Authorization header: JWT %HASH%

@app.route('/')
def running():
    return "Welcome to Dwellingly"


userList = [
    {
        "name": "Default User",
        "password": "userPassword",
        "username": "defaultUser",
        "email": "user1@dwellingly.com",
        "archived": "false",
        "uid": "user0"
    },
    {
        "name": "Default User2",
        "password": "userPassword",
        "username": "defaultUser2",
        "email": "user2@dwellingly.com",
        "archived": "false",
        "uid": "user1"
    }
]

# | POST   | `v1/users/`     | Creates a new user     |
# | GET    | `v1/users/`     | Gets all users         |
class Users(Resource):
    # @jwt_required()
    def get(self):
        return {"users": userList}

    def post(self):
         uid = "user" + str(len(userList)) #replace weith better id hash
         request_data = request.get_json()

         new_user = {
            "name": request_data["name"],
            "password": request_data["password"],
            "username": request_data["username"],
            "email": request_data["email"],
            "archived": "false",
            "uid":uid
            }
         userList.append(new_user)
        
         return new_user, 201

# | GET    | `v1/users/:uid` | Gets a single user     |
# | PATCH  | `v1/users/:uid` | Updates a single user  |
# | PUT    | `v1/users/:uid` | Archives a single user |
# | DELETE | `v1/users/:uid` | Deletes a single user  |

class User(Resource):
    # @jwt_required()
    #todo create request parser once we settle on user structure

    def get(self, uid):
        #finally get to show off my lamda functions...
        user = next(filter(lambda x: x["uid"] == uid, userList), None) 
        return {"user": user}, 200 if user else 404

    def patch(self, uid):
        user = next(filter(lambda x: x["uid"] == uid, userList), None) 
        # request_data = request.get_json()
        parser = reqparse.RequestParser()
        parser.add_argument('name', help="need a email") 
        parser.add_argument('password', required=True, help="need a password") 
        parser.add_argument('username', help="need a username") 
        parser.add_argument('email', help="need a email") 

        request_data = parser.parse_args()

        if user:
            user.update(request_data)
        return {"user": user}, 200 

    def put(self, uid):
        for user in userList:
            if user["uid"] == uid:
                if user["archived"] == "false":
                    user["archived"] = "true"
                else:
                    user["archived"] = "false"
                return user, 201
    
        return {"message": "User not found"}, 404

    def delete(self, uid):
        global userList
        userList = next(filter(lambda x: x["uid"] != uid, userList), None)
        return {"message": "user deleted"}
        
    

api.add_resource(Users, "/v1/users")
api.add_resource(User, "/v1/user/<string:uid>")

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
