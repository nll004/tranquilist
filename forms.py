from email import message
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, PasswordField
from wtforms.validators import InputRequired, Length, EqualTo


class AddUserForm(FlaskForm):
    '''Form for adding a new user'''

    username = StringField('Username', validators=[InputRequired(), Length(min=6, max=20)])
    fname = StringField('First Name', validators=[InputRequired(), Length(max=35)])
    lname = StringField('Last Name', validators=[InputRequired(), Length(max=45)])
    email = StringField('Email', validators=[InputRequired()])
    password = PasswordField('Create Password', validators=[InputRequired(), Length(min=8, message="Password must be at least 8 characters"),
                                                EqualTo('confirm_pwd', message='Passwords must match')])
    confirm_pwd = PasswordField('Confirm Password')


class AuthenticateForm(FlaskForm):
    '''Form for user login'''

    username = StringField('Username', validators=[InputRequired(), Length(min=6, max=20, message='Username must be between 6 and 20 characters long.')])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8)])


class TaskForm(FlaskForm):
    '''Form for creating and editing a task'''

    item = StringField()
    details = TextAreaField()
    list_id = SelectField

class NewList(FlaskForm):
    '''Form for creating and editing a list'''

    name = StringField()
    # sublist = SelectField() REq only on forms not db
