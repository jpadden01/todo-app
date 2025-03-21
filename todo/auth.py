from flask import Blueprint, render_template, request, redirect, url_for, flash

from . import db
from .models import User

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form.get('username')).first()
        if user.password != request.form.get('password'):
            flash('Incorrect password...')
            return render_template('login.html')
        flash('Logged in succesfully')
        return redirect(url_for('views.home'))
    return render_template('login.html')

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    # TODO: SIGN UP PAGE
    if request.method == 'POST':
        if User.query.filter_by(username=request.form.get('username')).first():
            flash('Username is already in use...')
            return render_template('signup.html')
        if request.form.get('password') != request.form.get('password-confirm'):
            flash('Passwords must match...')
            return render_template('signup.html')
        user = User(username=request.form.get('username'), 
                    password=request.form.get('password'))
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('signup.html')

@auth.route('/logout')
def logout():
    # TODO: LOG OUT
    return '<p>Log Out</p>'