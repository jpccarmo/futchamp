from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

from .config import config_by_name

# from .controller.home_controller import home_page
from .controller.home_controller import construct_home


db = SQLAlchemy()
flask_bcrypt = Bcrypt()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    db.init_app(app)
    flask_bcrypt.init_app(app)

    # app.register_blueprint(home_page, path='/')
    app.register_blueprint(construct_home(config_name), path='/')


    return app