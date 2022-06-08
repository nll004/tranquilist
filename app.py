from flask import Flask, render_template
from apis import get_events, get_quote
from models import connect_db, db

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///tranquilist'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

@app.route('/')
def display_home():
	'''Display info page for new users'''

	return render_template('home.html')

# @app.route('/signup')

# @app.route('/login')

@app.route('/mylists')
def show_user_page():
	'''User page after logging in. Show tasks and events.'''

	# if invalid user redirect to login or signup

	# if valid user and authenticated
	# get user and retrieve tasks/lists
	quote = get_quote()
	calendar_events = get_events()


	return render_template('home.html', quote = quote, events = calendar_events)
