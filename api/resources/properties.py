from flask import Blueprint
from flask_restful import Api, Resource


# | method | route                | action                     |
# | :----- | :------------------- | :------------------------- |
# | POST   | `v1/properties/`     | Creates a new property     |
# | GET    | `v1/properties/`     | Gets all properties        |
# | GET    | `v1/properties/:uid` | Gets a single property     |
# | PATCH  | `v1/properties/:uid` | Updates a single property  |
# | PUT    | `v1/properties/:uid` | Archives a single property |
# | DELETE | `v1/properties/:uid` | Deletes a single property  |

# single property resource
class Property(Resource):
    def get(self, uid):
        pass

    def patch(self, uid):
        pass

    def put(self, uid):
        pass

    def delete(self, uid):
        pass


# multiple property resources
class Properties(Resource):
    def get(self, uid):
        pass

    def post(self, uid):
        pass


# defines blueprint and instantiates blueprint
properties_api = Blueprint('resources.properties', __name__)

# instantiates API
api = Api()

#  define endpoints
api.add_resource(Property, "/v1/properties/<string:uid>")
api.add_resource(Properties, "/v1/properties")
