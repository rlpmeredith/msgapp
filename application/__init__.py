from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config
from flask_migrate import Migrate
from flask_login import LoginManager

db = SQLAlchemy()
# migrate = Migrate(app, db)
# login = LoginManager(app)
# login.login_view = 'login'

def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(Config)
    db.init_app(app)

    with app.app_context():

        # Imports
        from . import routes

        # # Create tables for our models
        # db.create_all()

        return app

# app = (__name__)
# app.config.from_object('Config')
# from app import routes, models

