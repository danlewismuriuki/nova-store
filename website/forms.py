from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, PasswordField, EmailField, BooleanField, SubmitField
from wtforms.validators import DataRequired, length, NumberRange

class SignUpForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired(), length(min=6)])
    password1 = PasswordField('Enter Your Password', validators=[DataRequired(), length(min=6)])
    password2 = PasswordField('Confirm Your Password', validators=[DataRequired(), length(min=6)])
    submit = SubmitField('sign Up')

class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired()])
    password2 = PasswordField('Confirm Your Password', validators=[DataRequired    (), length(min=6)])
    submit = SubmitField('Log in')

class PasswordChangedForm(FlaskForm):
    current_password = PasswordField('Current Password', validatrs=[DataRequired(), length(min=6)])
    new_password = PasswordField('New Password', validatrs=[DataRequired(), length(min=6)])
    confirm_new_password =  PasswordField('confirm New Password', validatrs=[DataRequired(), length(min=6)])
    change_password = SubmitField('change Password')
