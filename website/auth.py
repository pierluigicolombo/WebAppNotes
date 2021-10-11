'''
views for auth
'''


from flask import Blueprint

auth = Blueprint('auth', __name__)


@auth.route('login')
def login():
    '''
    function that handles the login
    '''
    return "<p>Login<p>"


@auth.route('logout')
def logout():
    '''
    function that handles the logout
    '''
    return "<p>Logout<p>"


@auth.route('sign-up')
def sign_up():
    '''
    function that handles the sign up
    '''
    return "<p>Sign-up<p>"
