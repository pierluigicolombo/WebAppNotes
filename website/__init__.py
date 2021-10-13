'''
create the app flask
'''


from flask import Flask
from .views import views
from .auth import auth
from flask_sqlalchemy import SQLAlchemy

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

    return app
