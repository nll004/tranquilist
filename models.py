from flask_sqlalchemy import SQLAlchemy
# from flask_bcrypt import Bcrypt

db = SQLAlchemy()
# bcrypt = Bcrypt()


def connect_db(app):
    '''Connect to database.'''

    db.app = app
    db.init_app(app)


class User(db.Model):
    '''User information'''

    __tablename__ = 'users'

    username = db.Column(db.String(20), primary_key=True, unique=True, nullable=False)
    fname = db.Column(db.String(35), nullable=False)
    lname = db.Column(db.String(45), nullable=False)
    email = db.Column(db.Text, nullable=False, unique=True)
    hashed_pwd = db.Column(db.Text, nullable=False)

    tasks = db.relationship('Task', backref='user', passive_deletes=True)

    lists = db.relationship('List', backref='user', passive_deletes=True)


class List(db.Model):
    '''Task lists for grouping individual tasks.
    Ex: Bills, Grocery List, Do Today, Homework, etc. '''

    __tablename__ = 'lists'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(25), nullable=False)
    user_username = db.Column(db.String(20), db.ForeignKey('users.username', ondelete='cascade'))
    sublist_id = db.Column(db.Integer, default=3)


class Task(db.Model):
    '''Stored tasks'''

    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    item = db.Column(db.String(30), nullable=False)
    details = db.Column(db.String(100), nullable=True)
    list_id = db.Column(db.Integer, db.ForeignKey('lists.id', ondelete='cascade'), nullable=False)
    user_username = db.Column(db.Text, db.ForeignKey('users.username', ondelete='cascade'), nullable=False)

    lists = db.relationship('List', backref='tasks', passive_deletes=True)
