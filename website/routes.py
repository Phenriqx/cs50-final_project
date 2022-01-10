from website import app, db, bcrypt
from website.forms import RegisterUser, LoginUser, AddTask
from website.models import User
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, current_user, logout_user, login_required

@app.route('/home')
@app.route('/')
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
        return redirect(url_for('layout'))
    
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


@app.route('/to-do-list')
def todo_list():
    task = AddTask()
    return render_template('todo_list.html', task=task)