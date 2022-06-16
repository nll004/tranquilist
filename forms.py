from models import TimeLine
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, PasswordField, HiddenField, BooleanField
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


class NewTasklistForm(FlaskForm):
    '''Form for creating a tasklist'''

    name = StringField('Task Name', validators=[InputRequired(), Length(max=30)])
    timeline = HiddenField('timeline_id', validators=[InputRequired(message="Something went wrong with your submission")])

class EditTasklistForm(FlaskForm):
    '''Form for editing a tasklist'''

    name = StringField('Task name', validators=[InputRequired(), Length(max=30)])
    time_line_id = SelectField('Timeline', choices=[(1, "Today"), (2, "Soon"), (3, "Later")])
    # time_line_id = SelectField('Timeline', choices = [(t.id, t.name) for t in TimeLine.query.all()])
    # RuntimeError: No application found. Either work inside a view function or push an application context. See http://flask-sqlalchemy.pocoo.org/contexts/.
    complete = BooleanField('Check if complete')


class SubtaskForm(FlaskForm):
    '''Form for creating and editing a subtask within a tasklist'''

    name = StringField('Name', validators=[InputRequired(), Length(max=30)])
    details = TextAreaField('Details', validators=[Length(max=100, message='Details cannot exceed 100 characters')])
    list_id = HiddenField('list_id', validators=[InputRequired(message='Something went wrong with your submission')])
