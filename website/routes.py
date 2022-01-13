import re
from website import app, db, bcrypt
from website.forms import RegisterUser, LoginUser, AddTask
from website.models import User, Task    
from flask import render_template, request, redirect, url_for, flash, session
from flask_login import login_user, current_user, logout_user, login_required


@app.route('/')
@login_required
def index():
    return render_template('layout.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('layout'))
    
    form = RegisterUser()
    if form.validate_on_submit():
        hash_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hash_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    form = LoginUser()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        check_hash_password = bcrypt.check_password_hash(user.password, form.password.data)
        if user and check_hash_password:
            login_user(user, remember=form.remember_me.data)
            return redirect(url_for('index'))
        else:
            flash('Login unsuccesful. Please check your email and password', 'danger')
        
    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/tasks', methods=['GET', 'POST'])
@login_required
def tasks():
    form = AddTask()

    if form.validate_on_submit():
        task = Task(task_description=form.task_description.data, author=current_user)
        db.session.add(task)
        db.session.commit()
        return redirect(url_for('todo_list'))
        
    tasks = Task.query.filter_by(author=current_user).all()
    return render_template('tasks.html', tasks=tasks, form=form)