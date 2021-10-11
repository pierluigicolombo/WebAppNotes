'''
general views
'''


from flask import Blueprint

views = Blueprint('views', __name__)


@views.route('/')
def home():
    '''
    home view
    '''
    return "<h1>HelloWorld! sqwdq<h1>"
