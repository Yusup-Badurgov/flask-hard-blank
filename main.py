from flask_mobility import Mobility
from flask import Flask
from flask_restx import Api

from config import Config
from setup_db import db

from views.movies import movies_ns
from views.directors import directors_ns
from views.genres import genres_ns


# функция создания основного объекта app
def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    return app


# функция подключения расширений (Flask-SQLAlchemy, Flask-RESTx, ...)
def register_extensions(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(movies_ns)
    api.add_namespace(directors_ns)
    api.add_namespace(genres_ns)
    with app.app_context():
        db.create_all()



app = create_app(Config())


if __name__ == '__main__':
    app.run(host="localhost", port=10001, debug=True)