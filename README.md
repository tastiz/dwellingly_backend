# dwellingly_backend

[![Build Status](https://travis-ci.com/codeforpdx/dwellingly_backend.svg?branch=api)](https://travis-ci.com/codeforpdx/dwellingly_backend)

Flask based Backend API for Dwellingly 



## Get Set Up


1) Clone the project

```bash
git clone https://github.com/codeforpdx/dwellingly_backend.git
```

2. cd into the directory of the project

```bash
cd dwellingly_backend
```



```bash
export FLASK_APP=api 

flask run

```

6. Open up [localhost:5000](http://localhost:5000)

## General Organization




###Directory tree
```bash
/dwellingly_backend
    |--api
    |   |--models
    |   |   |--__init__.py
    |   |    `--Sqlalchemy_models.py
    |   |--resources
    |   |   |--__init__.py
    |   |   |--properties.py
    |   |    `--users.py
    |   |--tests
    |   |   |--__init__.py
    |   |   |--conftest.py
    |   |   `--test_factory.py
    |   |--`__init.py__(application lives here)

```

### General Architecture
This flask project is using the flask application factory and flaskRestful model patterns

### application factory  example:
````
def create_app(config_filename):

    # aplication is defined
    app = Flask(__name__)

    # define configuration options
    app.config.from_pyfile(config_filename)

    # define database
    from yourapplication.model import db
    db.init_app(app)
    
    #  calls to views, blue prints, etc
    from yourapplication.views.admin import admin
    from yourapplication.views.frontend import frontend
    app.register_blueprint(admin)
    app.register_blueprint(frontend)

    return app
````
##### more info:
https://flask.palletsprojects.com/en/1.1.x/patterns/appfactories/#application-factories


