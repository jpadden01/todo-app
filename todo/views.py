from . import db
from .models import Task

from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import current_user, login_required

views = Blueprint("views", __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    if not current_user.is_authenticated:
        return redirect(url_for('auth.login'))
    if request.method == 'POST':
        task_id = request.form.get('delete')
        task = Task.query.filter_by(id=task_id).first()
        db.session.delete(task)
        db.session.commit()
        flash('Task deleted', category='success')
    return render_template('home.html')

@views.route('/task', methods=['GET', 'POST'])
@login_required
def task():
    if request.method == 'POST':
        task = Task(task=request.form.get('task'), user_id=current_user.id)
        db.session.add(task)
        db.session.commit()
        flash('Task created', category='success')
        return redirect(url_for('views.home'))
    return render_template('task.html')