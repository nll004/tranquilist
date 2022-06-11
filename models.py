from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()


def connect_db(app):
    '''Connect to database.'''

    db.app = app
    db.init_app(app)


class User(db.Model):
    '''User information'''

    __tablename__ = 'users'

    username = db.Column(db.String(20), primary_key=True, unique=True)
    fname = db.Column(db.String(35), nullable=False)
    lname = db.Column(db.String(45), nullable=False)
    email = db.Column(db.Text, nullable=False, unique=True)
    hashed_pwd = db.Column(db.Text, nullable=False)

    tasks = db.relationship('Task', backref='user', cascade='all, delete', passive_deletes=True)
    lists = db.relationship('List', backref='user', cascade='all, delete', passive_deletes=True)

    @classmethod
    def register_user(cls, username, fname, lname, email, pwd):
        '''Create new user with hashed pwd and return user'''

        hashed_pwd = bcrypt.generate_password_hash(pwd).decode('utf8')

        return cls(username=username, fname=fname,
                    lname=lname, email=email, hashed_pwd=hashed_pwd)

    @classmethod
    def authenticate(cls, username, pwd):
        '''Authenticate user to make sure username is valid and pwd is correct'''

        user = User.query.filter_by(username=username).first()
        correct_pwd = bcrypt.check_password_hash(user.hashed_pwd, pwd)

        if user and correct_pwd:
            return user
        else:

            return False

    @classmethod
    def delete_user(cls, username):

        user = User.query.filter_by(username=username)

        db.session.delete(user)
        db.session.commit()


class TimeLine(db.Model):
    '''Groups the tasks into a category or time line. Ex: Today, Soon, Later, etc.'''

    __tablename__ = 'time_lines'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(25), nullable=False)


class Task(db.Model):
    '''Stored tasks'''

    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    item = db.Column(db.String(30), nullable=False)
    details = db.Column(db.String(100), nullable=True)
    list_id = db.Column(db.Integer, db.ForeignKey('lists.id'))
    time_line_id = db.Column(db.Integer, db.ForeignKey('time_lines.id'))
    user_username = db.Column(db.Text, db.ForeignKey('users.username', ondelete='CASCADE'), nullable=False)

    time_line = db.relationship('TimeLine', backref='tasks')


class List(db.Model):
    '''Task lists that are located somewhere on the to do timeline and can also hold individual tasks'''

    __tablename__ = 'lists'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), nullable=False)
    time_line_id = db.Column(db.Integer, db.ForeignKey('time_lines.id'), default=3, nullable=False)
    user_username = db.Column(db.Text, db.ForeignKey('users.username', ondelete='CASCADE'), nullable=False)

    tasks = db.relationship('Task', backref='list', cascade='all, delete', passive_deletes=True)
    time_line = db.relationship('TimeLine', backref='lists')
