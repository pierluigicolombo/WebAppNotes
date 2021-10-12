'''
views for auth
'''


from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)


@auth.route('login', methods=['GET', 'POST'])
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


@auth.route('sign-up', methods=['GET', 'POST'])
def sign_up():
    '''
    function that handles the sign up
    '''
    if request.method == 'POST':
        email = request.form.get("email")
        firstName = request.form.get("firstName")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        # input check
        if len(email) < 4:
            flash('Email must be greater than 3 characters', category='error')
        elif len(firstName) < 2:
            flash('Email must be greater than 1 characters', category='error')
        elif password1 != password2:
            flash("password doesn't match", category='error')
        elif len(password1) < 7:
            flash("password too short, lenght must be at least 7 characters", category='error')
        else:
            # add user
            flash("user created", category='success')

    return render_template("sign_up.html")
