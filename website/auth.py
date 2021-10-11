'''
views for auth
'''


from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)


@auth.route('login')
def login():
    '''
    function that handles the login
    '''
    return render_template("login.html")


@auth.route('logout')
def logout():
    '''
    function that handles the logout
    '''
    return render_template("logout.html")


@auth.route('sign-up')
def sign_up():
    '''
    function that handles the sign up
    '''
    return render_template("sign_up.html")
