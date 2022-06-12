from app import app
from models import User, TaskList, Task, TimeLine, db, connect_db

connect_db(app)

def seed_db():
    db.drop_all()
    db.create_all()

    # =========================================================
    #   Populate the 3 unchanging timelines
    # =========================================================
    tl1 = TimeLine(name='Today')
    tl2 = TimeLine(name='Soon')
    tl3 = TimeLine(name='Later')

    db.session.add(tl1)
    db.session.add(tl2)
    db.session.add(tl3)
    db.session.commit()

    user1 = User.register_user(username='nll004', fname='Nate', lname='Lon', email='email@gmail.com', pwd='correct pwd')
    user2 = User.register_user(username='nll008', fname='Jim', lname='Jones', email='email2@gmail.com', pwd='correct pwd')

    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()

    l1 = TaskList(name='Wash Dishes', time_line_id=1, user_username = 'nll004')
    l2 = TaskList(name='Groceries', time_line_id=1, user_username = 'nll004')
    l3 = TaskList(name='Water Plants', time_line_id=2, user_username = 'nll004')
    l4 = TaskList(name='Mow Yard', user_username = 'nll004')
    l5 = TaskList(name='Pay Bills', time_line_id =2, user_username = 'nll004')
    l6 = TaskList(name='Sell dresser', user_username = 'nll004', complete=True)
    l7 = TaskList(name='Buy new shoes', user_username = 'nll004', complete=True)
    l8 = TaskList(name='Fix sink', time_line_id='1', user_username='nll008')
    l9 = TaskList(name='Hair cut', complete=True, time_line_id='1', user_username='nll004')

    db.session.add(l1)
    db.session.add(l2)
    db.session.add(l3)
    db.session.add(l4)
    db.session.add(l5)
    db.session.add(l6)
    db.session.add(l7)
    db.session.add(l8)
    db.session.add(l9)
    db.session.commit()

    t1 = Task(name='Milk', list_id=2)
    t2 = Task(name='Eggs', list_id=2)
    t3 = Task(name='Chocolate', list_id=2 , details='Just buy 1 bar', complete=True)
    t4 = Task(name='Buy gas', list_id=4 , details='Need help from nll008')
    t5 = Task(name='Internet', list_id=5, details='Set up autopay')
    t6 = Task(name='Water bill', list_id=5 , details='Before 6/30/22')
    t7 = Task(name='Gas bill', list_id=5, complete=True)
    t8 = Task(name='Electric', list_id=5, complete=True)
    t9 = Task(name='Buy faucet', list_id=8)
    t10 = Task(name='Borrow pipe wrench', list_id=8 , details='Borrow from Chris', complete=True)

    db.session.add(t1)
    db.session.add(t2)
    db.session.add(t3)
    db.session.add(t4)
    db.session.add(t5)
    db.session.add(t6)
    db.session.add(t7)
    db.session.add(t8)
    db.session.add(t9)
    db.session.add(t10)
    db.session.commit()

print('Ran seed file')

if __name__ == '__main__':
    seed_db()
