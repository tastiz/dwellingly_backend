from flask import Flask
import os

from api.resources.properties import properties_api
from api.resources.users import user_api


def create_app(test_config=None):
    """
    This is an application factory pattern

    essentially a function that defines the application,
    loads defined configurations initializes the database file,
    and registers blueprints that hold logic for api endpoints,
    :var
    app: flask application


    :rtype: object: Flask application,
    """
    # Flask app defined
    # config files are relative to the instance folder
    app = Flask(__name__, instance_relative_config=True)

    # register blueprints for that hold logic for endpoints
    app.register_blueprint(properties_api)
    app.register_blueprint(user_api)

    #  some default config here
    app.config.from_mapping(
        DEBUG=True,

        )

    try:
        # creates instance dir
        os.makedirs(app.instance_path)
    except OSError:
        pass

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('', silent=True)
    else:
        # load the test config if passed in this case test/conftest
        app.config.update(test_config)

    # test route
    @app.route('/')
    def hello():
        return 'welcome to dwellingly'

    return app
