from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user

from . import db
from .models import User

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form.get('username')).first()
        if user.password != request.form.get('password'):
            flash('Incorrect password', category='danger')
            return render_template('login.html')
        login_user(user)
        flash('Logged in succesfully', category='success')
        return redirect(url_for('views.home'))
    return render_template('login.html')

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        if User.query.filter_by(username=request.form.get('username')).first():
            flash('Username is already in use', category='danger')
            return render_template('signup.html')
        if request.form.get('password') != request.form.get('password-confirm'):
            flash('Passwords must match', category='danger')
            return render_template('signup.html')
        user = User(username=request.form.get('username'), 
                    password=request.form.get('password'))
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('signup.html')

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('views.home'))