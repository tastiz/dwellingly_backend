from flask import Blueprint
from flask_restful import Api, Resource, reqparse
from flask_jwt import jwt_required

# | POST   | `v1/users/`     | Creates a new user     |
# | GET    | `v1/users/`     | Gets all users         |


class Users(Resource):
    @jwt_required()
    def get(self):
        return {"users": userList}

    def post(self):
         uid = "user" + str(len(userList)) #replace with better id hash
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

# | method | route                | action                     |
# | :----- | :------------------- | :------------------------- |
# | POST   | `v1/properties/`     | Creates a new property     |
# | GET    | `v1/properties/`     | Gets all properties        |
# | GET    | `v1/properties/:uid` | Gets a single property     |
# | PATCH  | `v1/properties/:uid` | Updates a single property  |
# | PUT    | `v1/properties/:uid` | Archives a single property |
# | DELETE | `v1/properties/:uid` | Deletes a single property  |


# instantiate Blueprint
user_api = Blueprint('resources.users', __name__)

# instantiate API and add resources
api = Api()
api.add_resource(Users, "/v1/users")
api.add_resource(User, "/v1/users/<string:uid>")