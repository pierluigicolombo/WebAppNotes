'''
create the app flask
'''

from os import path
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .views import views
from .auth import auth



db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    '''
    create the app flask
    '''
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'WQQXQxwecwedwedwxw'  # ENCRYPT AND SECURE THE
    # COOKIE AND SESSION DATA
    app.config["SQLALCHEMY_DATABASE_URI"] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note

    create_database(app)
    return app


def create_database(app):
    '''
    create database if not exists
    '''
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print("created database")
