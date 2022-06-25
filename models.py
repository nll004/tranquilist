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

    lists = db.relationship('TaskList', backref='user', cascade='all, delete', passive_deletes=True)

    @classmethod
    def register_user(cls, username, fname, lname, email, pwd):
        '''Create new user with hashed pwd and return user'''

        hashed_pwd = bcrypt.generate_password_hash(pwd).decode('utf8')

        new_user = User(username=username, fname=fname,
                    lname=lname, email=email, hashed_pwd=hashed_pwd)
        db.session.add(new_user)
        db.session.commit()

        return new_user

    @classmethod
    def authenticate(cls, username, pwd):
        '''Authenticate user to make sure username is valid and pwd is correct'''

        user = User.query.filter_by(username=username).first()

        if user:
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
    '''Subtasks located in tasklists'''

    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(35), nullable=False)
    details = db.Column(db.String(100), nullable=True)
    complete = db.Column(db.Boolean, default=False, nullable=False)
    list_id = db.Column(db.Integer, db.ForeignKey('task_lists.id', ondelete='CASCADE'), nullable=False)


class TaskList(db.Model):
    '''Task lists that are located somewhere on the to do timeline and can also hold individual subtasks'''

    __tablename__ = 'task_lists'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(35), nullable=False)
    complete = db.Column(db.Boolean, default=False, nullable=False)
    time_line_id = db.Column(db.Integer, db.ForeignKey('time_lines.id'), default=3, nullable=False)
    user_username = db.Column(db.Text, db.ForeignKey('users.username', ondelete='CASCADE'), nullable=False)

    subtasks = db.relationship('Task', backref='tasklists', cascade='all, delete', passive_deletes=True)
    time_line = db.relationship('TimeLine', backref='lists')
