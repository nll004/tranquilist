from app import app
from models import connect_db, db, User, Task, List

connect_db(app)

user1 = User(username='nll004', fname='Nate', lname='Lond', email='email@gmail.com', hashed_pwd='login')

db.session.add(user1)
db.session.commit()

l1 = List(name='Today', user_username='nll004', sublist_id=0)
l2 = List(name='Soon', user_username='nll004', sublist_id=0)
l3 = List(name='Future', user_username='nll004', sublist_id=0)
l4 = List(name='Bills', user_username='nll004', sublist=2)
l5 = List(name='Groceries', user_username='nll004')

db.session.add(l1)
db.session.add(l2)
db.session.add(l3)
db.session.add(l4)
db.session.add(l5)
db.session.commit()

t1 = Task(item='Wash Dishes', list_id='1', user_username='nll004')
t2 = Task(item='Workout', list_id='1', details='Chest and legs', user_username='nll004')
t3 = Task(item='Mow Yard', list_id='2', user_username='nll004')
t4 = Task(item='Pay electric bill', list_id='4', details='Due 6/25/22', user_username='nll004')
t5 = Task(item='Schedule dentist', list_id='3', details='phone# 304/538/1746', user_username='nll004')
t6 = Task(item='Wash car', list_id='2', user_username='nll004')
t7 = Task(item='Laundry soap', list_id='5' user_username='nll004')
t8 = Task(item='Milk', list_id='5' user_username='nll004')
t9 = Task(item='Eggs', list_id='5' user_username='nll004')

db.session.add(t1)
db.session.add(t2)
db.session.add(t3)
db.session.add(t4)
db.session.add(t5)
db.session.add(t6)
db.session.add(t7)
db.session.add(t8)
db.session.add(t9)
db.session.commit()
