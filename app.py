from flask import Flask, render_template, redirect, session
from apis import get_events, get_quote
from models import connect_db, db, User
from forms import AddUserForm, AuthenticateForm
from keys import secret_key

CURRENT_USERNAME = None

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///tranquilist'
app.config['SECRET_KEY'] = secret_key
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)


def login(username):
	'''Take username and store in session.'''

	# g.user = User.query.get(username)
	# print('G USER: =====================', g.user)

	CURRENT_USERNAME = username
	print('Current username:', CURRENT_USERNAME)

	session[CURRENT_USERNAME] = CURRENT_USERNAME
	print('Username added to session?')
	print(session[CURRENT_USERNAME])


#  Logout not working ===================================================================
@app.route('/logout')
def logout():
	'''Remove user from session and g.user'''

	print('Before logout session', session.get('CURRENT_USERNAME'))
	if CURRENT_USERNAME in session:
		print('Current username is in session---')

		del session[CURRENT_USERNAME]
	print('No the current username is not in the session')
	print('aFTER LOGOUT==========', session[CURRENT_USERNAME])
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


# @app.route('/mylists')
# def show_user_page():
# 	'''User page after logging in. Show tasks and events.'''

# 	# if correct user then display
# 	# print("List home with G User? =========================", g.user)
# 	user = User.query.get(CURRENT_USERNAME)
# 	print('CURRENT USER:', CURRENT_USERNAME)
# 	print('QUERIED USER', user)
# 	# if invalid user redirect to login or signup

# 	# if valid user and authenticated
# 	# get user and retrieve tasks/lists
# 	quote = get_quote()
# 	calendar_events = get_events()

# 	return render_template('user_home.html', quote = quote, events = calendar_events)


@app.route('/mylists/<username>')
def show_user_page(username):
	'''User page after logging in. Show tasks and events.'''

	# this method cant confirm user unless flask sesssions is working
	# if correct user then display page else redirect to login
	user = User.query.get(username)
	print('CURRENT USER:', CURRENT_USERNAME)
	print('QUERIED USER', user)
	# if invalid user redirect to login or signup

	# if valid user and authenticated
	# get user and retrieve tasks/lists
	quote = get_quote()
	calendar_events = get_events()

	return render_template('user_home.html', quote = quote, events = calendar_events, user=user)
