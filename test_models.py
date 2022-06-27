# run tests with:
# python -m unittest -v test_models.py

from app import app
from models import TaskList, connect_db, db, User, bcrypt
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


class TaskModelTestCase(TestCase):
    '''Test tasks model'''

    def test_user_tasklists(self):
        # can you access tasks from user using relationship?
        self.assertTrue(user1)
        self.assertEqual(user1.lists[0].name, 'Wash Dishes')
        self.assertEqual(user1.lists[0].id, 1)


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
