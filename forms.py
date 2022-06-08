from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, PasswordField
from wtforms.validators import InputRequired, Length


class AddUserForm(FlaskForm):
    '''Form for adding a new user'''

    username = StringField('Username', validators=[InputRequired(), Length(min=6, max=20)])
    fname = StringField('First Name')
    lname = StringField('Last Name')
    email = StringField('Email')
    password = PasswordField('Create Password', validators=[InputRequired(), Length(min=8), ])
    confirm_pwd = PasswordField('Confirm Password')

class TaskForm(FlaskForm):
    '''Form for creating and editing a task'''

    item = StringField()
    details = TextAreaField()
    list_id = SelectField

class NewList(FlaskForm):
    '''Form for creating and editing a list'''

    name = StringField()
    # sublist = SelectField() REq only on forms not db
