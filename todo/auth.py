from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    # TODO: LOGIN PAGE
    return '<p>Log In</p>'

@auth.route('/signup')
def signup():
    # TODO: SIGN UP PAGE
    return '<p>Sign Up</p>'

@auth.route('/logout')
def logout():
    # TODO: LOG OUT
    return '<p>Log Out</p>'