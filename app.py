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
	'''Display home for user'''

	quote = get_quote()
	calendar_events = get_events()

	# for event in calendar_events:
		# date = event['start']
		# summary = event['summary']
		# link = event['htmlLink']
		# print('===================================Terminal:', start, summary, link)

	return render_template('home.html', quote = quote, events = calendar_events)
