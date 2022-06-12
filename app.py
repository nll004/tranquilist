from flask import Flask, render_template, redirect, session, g
from apis import get_calendar_events, get_quote
from models import connect_db, db, User
from forms import AddUserForm, AuthenticateForm
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
	'''If logged in, add current user to Flask global object.'''

	if CURRENT_USER in session:
		g.user = User.query.get(session['username'])
	else:
		g.user = None


@app.route('/login', methods=['GET', 'POST'])
def user_login():
	'''Display login form and handle authentication'''

	form = AuthenticateForm()

	if form.validate_on_submit():
		username = form.username.data
		password = form.password.data

		user = User.authenticate(username=username, pwd=password)

		if user:
			login(user.username)
			return redirect("/mylists")
		else:
			form.username.errors = ["Incorrect username or password"]

	return render_template('login.html', form=form)


@app.route('/logout')
def logout():
	'''Remove user from session and g.user'''

	if CURRENT_USER in session:
		del session[CURRENT_USER]

	return redirect('/')


@app.route('/')
def display_home():
	'''Display info page for new users'''

	return render_template('app_home.html')


@app.route('/register', methods=['GET', 'POST'])
def go_sign_up():
	'''Displays registration page and handles registration form submission'''

	form = AddUserForm()

	if form.validate_on_submit():
		user = User.register_user(username=form.username.data,
								fname=form.fname.data,
								lname=form.lname.data,
								email=form.email.data,
								pwd=form.password.data)
		db.session.add(user)
		db.session.commit()

		login(user.username)

		return redirect('/mylists')

	return render_template('register.html', form=form)


@app.route('/mylists')
def show_user_page():
	'''User page after logging in. Show tasks and events.'''

	# this method cant confirm user unless flask sesssions is working
	# if correct user then display page else redirect to login


	# if invalid user redirect to login or signup

	# if valid user and authenticated
	# get user and retrieve tasks/lists
	quote = get_quote()
	calendar_events = get_calendar_events()

	return render_template('user_home.html', quote = quote, events = calendar_events, user=g.user)
