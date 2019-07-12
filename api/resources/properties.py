from flask import Blueprint
from flask_restful import Api, Resource


# single property resource
class Property(Resource):
    def get(self,uid):
        pass

    def patch(self,uid):
        pass

    def put(self, uid):
        pass

    def delete(self, uid):
        pass

# multiple property resources
class Properties(Resource):
    def get(self,uid):
        pass

    def post(self,uid):
        pass


# defines blueprint and instantiates blueprint
properties_api = Blueprint('resources.properties', __name__)

# instantiates API
api = Api()

#  define endpoints
api.add_resource(Property, "/v1/properties/<string:uid>")
api.add_resource(Properties, "/v1/properties")