'''
general views
'''


from flask import Blueprint, render_template

views = Blueprint('views', __name__)


@views.route('/')
def home():
    '''
    home view
    '''
    return render_template("home.html")
