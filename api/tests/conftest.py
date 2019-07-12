import pytest
from api import create_app

@pytest.fixture()
def app():
    """
    returns a instance of the application object with testing config

    :var app: function
    :rtype: object: Flask_application
    """
    app = create_app({
        'TESTING': True,
        })

    return app


@pytest.fixture
def client(app):
    """
    Instantiates an instance of the flask test_client

    this provides a test_client to each test which allows access
    to the Http request and response also

    :return flask test_client
    :rtype: object
    :param app: Flask_application test configuration
    :type app: object
    """
    # TODO setup and teardown test DB

    return app.test_client()

