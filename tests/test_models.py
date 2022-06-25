# run tests with:
# python -m unittest -v tests/test_models.py
import sqlalchemy
import psycopg2
from app import app
from models import TaskList, connect_db, db, User, TimeLine, bcrypt
from seed import seed_db
from unittest import TestCase

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///tranquilist_test'
app.config['TESTING'] = True

connect_db(app)
db.drop_all()
db.create_all()
seed_db()

# Set up global users to test
user1 = User.query.get('nll004')
user2 = User.query.get('nll008')
# invalid user for testing
user3 = User.query.get('nll028')


#  Test User model
# ----------------------------------------------
class UserModelTestCase(TestCase):
    '''Test user model for valid signup and password hashing'''

    def test_user_signup(self):
        '''Test global users for registration'''

        # does user exist?
        self.assertIsNone(user3)
        self.assertTrue(user1)
        # is user an instance of User class?
        self.assertIsInstance(user1, User)


    def test_user_authenticate(self):
        '''Test valid user for user/hashed_pwd authentication'''

        # does valid user have hashed_pwd value?
        self.assertTrue(user1.hashed_pwd)
        # is the pwd hashed?
        self.assertNotEqual(user1.hashed_pwd, 'string text pwd')
        # does the authentication method work?
        self.assertFalse(bcrypt.check_password_hash(user1.hashed_pwd, 'wrong pwd'))
        self.assertTrue(bcrypt.check_password_hash(user1.hashed_pwd, 'correct pwd'))


    def test_user_signup_errors(self):
        '''Test for errors when creating a username or email that is already in the database'''

        # error if username is already taken
        # sqlalchemy.exc.IntegrityError:(psycopg2.errors.UniqueViolation) duplicate key value violates unique constraint "users_pkey"
        # DETAIL:  Key (username)=(nll004) already exists.

        # recreate existing user should throw unique constraint error
        self.assertRaises(psycopg2.errors.UniqueViolation, User.register_user(username='nll004', fname='null', lname='null',
                                                            email='another@email.com', pwd='password123'))
        self.assertRaises(sqlalchemy.exc.IntegrityError, User.register_user(username='nll004', fname='null', lname='null',
                                                             email='another@email.com', pwd='password123'))
        # db.session.rollback()
        # error if email is already used


class TaskModelTestCase(TestCase):
    '''Test tasks model'''

    def test_user_tasklists(self):
        # can you access tasks from user using relationship?
        self.assertTrue(user1)
        self.assertEqual(user1.lists[0].name, 'Wash Dishes')
        self.assertEqual(user1.lists[0].id, 1)


    def test_tasklist_relationships(self):
        '''Test user and task relationship'''

        # if you delete a user, all tasks associated to user should be deleted

        # ====================================================================================
        # not working? why wont db.session.delete(user2) work?
        # doesn't have to do with scopes
        # is it the way I queried the users?
        # I'm pretty sure it has to do with connecting to the test db

        # DetachedInstanceError: Parent instance <User at 0x7ff143d47550> is not bound to a Session;
        # lazy load operation of attribute 'tasks' cannot proceed (Background on this error at: https://sqlalche.me/e/14/bhk3)
        db.session.delete(user2)
        db.session.commit()

        # user = User.query.filter(User.username == 'nll008')
        # db.session.delete(user)
        # db.session.commit()

        # AttributeError: 'BaseQuery' object has no attribute '_sa_instance_state'
        # sqlalchemy.orm.exc.UnmappedInstanceError: Class 'flask_sqlalchemy.BaseQuery' is not mapped
        # self.assertFalse(user2)

        # Task.query.get(1) should cause an error


    def test_list_task_relationships(self):
        '''Test tasklist relationships'''
        tasklist = TaskList.query.get(2)

        self.assertTrue(tasklist)

        # do the tasklist have a timeline_id?
        self.assertTrue(tasklist.time_line)
        self.assertEqual(tasklist.time_line.id, tasklist.time_line_id)

        # does the tasklist have subtasks
        self.assertTrue(tasklist.subtasks)
        self.assertEqual(tasklist.subtasks[0].name, 'Milk')

        # if you delete a tasklist, the subtasks should delete






class ListModelTestCase(TestCase):
    '''Test lists model'''
    # can you access lists from user using relationship?
    # can you access tasks in the list?
    # if user is deleted the list should delete?
    # if task is deleted the list should not be deleted
    pass
