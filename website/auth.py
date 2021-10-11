'''
views for auth
'''


from flask import Blueprint

auth = Blueprint('auth', __name__)


@auth.route('login')
def login():
    '''
    function that handle the login
    '''
    return "<p>Login<p>"


@auth.route('logout')
def logout():
    '''
    function that handle the logout
    '''
    return "<p>Logout<p>"


@auth.route('signin')
def signin():
    '''
    function that handle the signin
    '''
    return "<p>Signin<p>"
