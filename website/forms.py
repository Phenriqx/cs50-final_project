from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.fields.simple import TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegisterUser(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=16)], render_kw={'placeholder': 'Username'})
    
    email = StringField('Email', validators=[DataRequired(), Email()], render_kw={'placeholder': 'Email'})
    
    password = PasswordField('Password', validators=[DataRequired()], render_kw={'placeholder': 'Password'})
    
    confirm_password  = PasswordField('ConfirmPassword', validators=[DataRequired(), EqualTo('password')], render_kw={'placeholder': 'Confirm Password'})
    
    submit = SubmitField('Sign Up')
    
    
class LoginUser(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()], render_kw={'placeholder': 'Email'})
    
    password = PasswordField('Password', validators=[DataRequired()], render_kw={'placeholder': 'Password'})
    
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Log in')
    

class AddTask(FlaskForm):
    task_description = StringField('Task Description', validators=[DataRequired()], render_kw={'placeholder': 'Task Description'})
    
    submit = SubmitField('Add Task')