from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user, login_required

views = Blueprint("views", __name__)

@views.route('/')
def home():
    if current_user.is_authenticated:
        return render_template('home.html')
    return redirect(url_for('auth.login'))

@views.route('/task', methods=['GET', 'POST'])
@login_required
def task():
    return render_template('task.html')