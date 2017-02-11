from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

from config import get_config

db = SQLAlchemy()
login_manager = LoginManager()

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(get_config(config_name))
    app.config.from_pyfile('secrets.py')
    login_manager.init_app(app)
    login_manager.login_message = "Please Log in to access this page"
    login_manager.login_view = 'auth.login'
    db.init_app(app)
    migrate = Migrate(app, db)
    from app import models

    return app


