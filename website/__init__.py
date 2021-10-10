'''
create the app flask
'''


from flask import Flask
from .views import views
from .auth import auth


def create_app():
    '''
    create the app flask
    '''
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'WQQXQxwecwedwedwxw'  # ENCRYPT AND SECURE THE
    # COOKIE AND SESSION DATA

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
   
    return app
