'''
views for auth
'''


import re
from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db

auth = Blueprint('auth', __name__)


@auth.route('login', methods=['GET', 'POST'])
def login():
    '''
    function that handles the login
    '''
    if request.method=='POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully', category='success')
            else:
                flash('incorrect password, try again', category='error')
        else:
            flash("user doesn't exist", category='error')
    
    return render_template("login.html")


@auth.route('logout')
def logout():
    '''
    function that handles the logout
    '''
    return render_template("logout.html")


@auth.route('sign-up', methods=['GET', 'POST'])
def sign_up():
    '''
    function that handles the sign up
    '''
    if request.method == 'POST':
        email = request.form.get("email")
        first_name = request.form.get("firstName")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        # input check
        user = User.query.filter_by(email=email).first()
        if user:
            flash('email already exist', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters', category='error')
        elif len(first_name) < 2:
            flash('FirstName must be greater than 1 characters', 
                  category='error')
        elif password1 != password2:
            flash("password doesn't match", category='error')
        elif len(password1) < 7:
            flash("password too short, lenght must be at least 7 characters", 
                  category='error')
        else:
            # add user
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()

            flash("user created", category='success')

            return redirect(url_for('views.home'))

    return render_template("sign_up.html")
