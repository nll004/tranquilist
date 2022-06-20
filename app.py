from flask import Flask, flash, render_template, redirect, session, g
from datetime import datetime
from apis import get_calendar_events, get_quote
from models import TaskList, TimeLine, connect_db, db, User, Task
from forms import AddUserForm, AuthenticateForm, EditTasklistForm, NewTasklistForm, SubtaskForm
from secret.keys import secret_key

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
		user = User.register_user(username=form.new_username.data,
								fname=form.fname.data,
								lname=form.lname.data,
								email=form.email.data,
								pwd=form.new_password.data)
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

	# get quote and calendar events
	quote = get_quote()

	# pass user into get_calendar_events to retrieve 1 week of personal google calendar events
	calendar_events = get_calendar_events(g.user)

	# format dates into a dateTime obj and add to calendar event obj as "newStart"
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

	print('Calendar events ==================')
	sorted_calendar_events = sorted(calendar_events, key=lambda x: datetime.strptime(x['newStart']['date'], '%a %m/%d'))
	print(sorted_calendar_events)

	# html forms =============================
	add_task_form = NewTasklistForm()
	add_subtask_form = SubtaskForm()
	edit_tasklist_form = EditTasklistForm()
	# edit_subtask_form =
	# ========================================

	return render_template('user_home.html', quote = quote,
						events = sorted_calendar_events, user=g.user,
						timelines=time_lines, task_form=add_task_form,
						subtask_form=add_subtask_form, edit_tasklist_form= edit_tasklist_form)


# =============================================================================
#                Manage TaskList and Subtasks
# =============================================================================

@app.route('/tasks/new', methods=['POST'])
def create_tasklist():
	'''Create new tasklists'''

	if not g.user:
		return redirect('/')

	form = NewTasklistForm()

	if form.validate_on_submit():
		tasklist = TaskList(name=form.new_tasklist_name.data,
						time_line_id= form.tasklist_timeline.data,
						user_username=g.user.username)
		db.session.add(tasklist)
		db.session.commit()

		return redirect('/mylists')

	else:
		return redirect('/')


@app.route('/tasks/edit', methods=['POST'])
def edit_tasklist():
	'''Select a task and edit'''

	if not g.user:
		return redirect('/')

	form = EditTasklistForm()

	if form.validate_on_submit():
		task = TaskList.query.get(form.edit_tasklist_id.data)
		task.time_line_id = form.tasklist_timeline_id.data
		task.name = form.edit_tasklist_name.data

		db.session.add(task)
		db.session.commit()

	return redirect('/mylists')


@app.route('/tasks/<int:task_id>/del')
def delete_tasklist(task_id):
	'''Delete selected task list. This should also remove all related subtasks'''

	if not g.user:
		return redirect('/')

	task = TaskList.query.get(task_id)

	db.session.delete(task)
	db.session.commit()

	return redirect('/mylists')


# ==================== Subtasks =========================

@app.route('/tasks/subtask/new', methods=['POST'])
def create_subtask():
	'''Save new subtask to database'''

	form = SubtaskForm()

	if form.validate_on_submit():

		subtask = Task(name=form.subtask_name.data,
						details=form.subtask_details.data or None,
						list_id= form.tasklist_id.data)
		db.session.add(subtask)
		db.session.commit()

		return redirect('/mylists')


# @app.route('/tasks/subtask/<int:subtask_id>/del')
# def delete_subtask(subtask_id):
# 	'''Delete subtask from tasklist'''

# 	if not g.user:
# 		return redirect('/')

# 	subtask = Task.query.get(subtask_id)

# 	db.session.delete(subtask)
# 	db.session.commit()

# 	return redirect('/mylists')
