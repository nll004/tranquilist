from calendar import calendar
from flask import Flask, flash, render_template, redirect, session, g
from requests import request
from datetime import datetime
from apis import get_calendar_events, get_quote
from models import TaskList, TimeLine, connect_db, db, User, Task
from forms import AddUserForm, AuthenticateForm, EditTasklistForm, NewTasklistForm, SubtaskForm
from keys import secret_key

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///tranquilist'
app.config['SECRET_KEY'] = secret_key
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False

CURRENT_USER = 'username'

connect_db(app)


def login(username):
	'''Take username and store in session.'''

	session[CURRENT_USER] = username


@app.before_request
def add_user_to_g():
	'''If "logged in" and username is in session, add current user to Flask global object.'''

	if CURRENT_USER in session:
		g.user = User.query.get(session['username'])
	else:
		g.user = None


@app.route('/login', methods=['POST'])
def user_login():
	'''Handle authentication and login'''

	form = AuthenticateForm()

	# validates CSRF token
	if form.validate_on_submit():
		username = form.username.data
		password = form.password.data

		# checks user password with hashed pwd in database
		user = User.authenticate(username=username, pwd=password)

		if user:
			# stores username to session
			login(user.username)
			return redirect("/mylists")
		else:
			form.username.errors = ["Incorrect username or password"]

	return


@app.route('/logout')
def logout():
	'''Remove username from session'''

	if CURRENT_USER in session:
		del session[CURRENT_USER]

	return redirect('/')


@app.route('/register', methods=['POST'])
def user_sign_up():
	'''Accepts new user registration form and creates new user'''

	form = AddUserForm()

	if form.validate_on_submit():
		# Create user, hash password and store in database
		user = User.register_user(username=form.username.data,
								fname=form.fname.data,
								lname=form.lname.data,
								email=form.email.data,
								pwd=form.password.data)
		db.session.add(user)
		db.session.commit()

		# add username to session
		login(user.username)

		return redirect('/mylists')
	return redirect('/')


@app.route('/')
def display_home():
	'''Display home page for new users'''

	signup_form = AddUserForm()
	login_form = AuthenticateForm()

	return render_template('app_home.html', signup_form=signup_form, login_form=login_form)


@app.route('/mylists', methods=['GET'])
def show_user_home():
	'''User page after logging in. Show tasks and events.'''

	# if correct user then display page else redirect to login
	if not g.user:
		return redirect('/')

	time_lines = TimeLine.query.all()
	# forms
	add_task_form = NewTasklistForm()
	add_subtask_form = SubtaskForm()
	edit_tasklist_form = EditTasklistForm()

	quote = get_quote()

	calendar_events = get_calendar_events()
	# format dates into a dateTime obj for use on user_home.html
	for event in calendar_events:

		if event['start'].get('dateTime'):
			dt = event['start'].get("dateTime").rsplit('-', 1)
			datetime_obj = datetime.strptime(dt[0], '%Y-%m-%dT%H:%M:%S')
			date = datetime_obj.strftime('%a %m/%d')
			time = datetime_obj.strftime('%H:%M')
			newStart = {'date': date, 'time': time}

		elif event['start'].get('date'):
			dt = event['start'].get('date')
			datetime_obj = datetime.strptime(dt, '%Y-%m-%d' )
			date = datetime_obj.strftime('%a %m/%d')
			newStart = {'date': date}

		event['newStart'] = newStart

	return render_template('user_home.html', quote = quote,
						events = calendar_events, user=g.user,
						timelines=time_lines, task_form=add_task_form,
						subtask_form=add_subtask_form, edit_tasklist_form= edit_tasklist_form)


# =============================================================================
#                Manage Tasks
# =============================================================================

@app.route('/tasks/new', methods=['POST'])
def create_tasklist():
	'''Save a new tasklist to database'''

	# if g.user.username == route username:
		# then post, patch, delete
	# e
	form = NewTasklistForm()

	if form.validate_on_submit():

		tasklist = TaskList(name=form.name.data,
						time_line_id= form.timeline.data,
						user_username=g.user.username)
		db.session.add(tasklist)
		db.session.commit()

		return redirect('/mylists')

# @app.route('/tasks/<int:task_id>/edit', methods=['POST'])
# def edit_tasklist(task_id):
# 	'''Select a task and edit'''

# 	return




@app.route('/tasks/subtask/new', methods=['POST'])
def create_subtask():
	'''Save new subtask to database'''

	form = SubtaskForm()

	if form.validate_on_submit():

		subtask = Task(name=form.name.data,
						details=form.details.data or None,
						list_id= form.list_id.data)
		db.session.add(subtask)
		db.session.commit()

		return redirect('/mylists')
