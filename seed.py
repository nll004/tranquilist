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

    l1 = TaskList(name='Task1', time_line_id=1, user_username = 'nll004')
    l2 = TaskList(name='Task2', time_line_id=1, user_username = 'nll004')
    l3 = TaskList(name='Task3', time_line_id=2, user_username = 'nll004')
    l4 = TaskList(name='Task4', user_username = 'nll004')
    l5 = TaskList(name='Task5', time_line_id =2, user_username = 'nll004')
    l6 = TaskList(name='Task6', user_username = 'nll004')
    l7 = TaskList(name='Task7', user_username = 'nll004')
    l8 = TaskList(name='Task1', time_line_id='1', user_username='nll008')
    l9 = TaskList(name='Task8', complete=True, time_line_id='1', user_username='nll004')

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

    t1 = Task(name='Subtask1', list_id=2 , details='Need help from nll008', complete=True)
    t2 = Task(name='Subtask2', list_id=2 , details='Need help from nll008')
    t3 = Task(name='Subtask3', list_id=2 , details='Need help from nll008')
    t4 = Task(name='Subtask1', list_id=4 , details='Need help from nll008')
    t5 = Task(name='Subtask2', list_id=4 , details='Need help from nll008')
    t6 = Task(name='Subtask1', list_id=5 , details='Need help from nll008')
    t7 = Task(name='Subtask2', list_id=5 , details='Need help from nll008')
    t8 = Task(name='Subtask3', list_id=5 , details='Need help from nll008', complete=True)
    t9 = Task(name='Subtask1', list_id=8 , details='Need help from nll008')
    t10 = Task(name='Subtask2', list_id=8 , details='Need help from nll008')

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
