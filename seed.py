from app import app
from models import connect_db, db, User, Task, TimeLine, List

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
    user2 = User.register_user(username='nll008', fname='Jim', lname='Lon', email='email2@gmail.com', pwd='correct pwd')

    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()

    l1 = List(name='Groceries', time_line_id=1, user_username = 'nll004')
    l2 = List(name='Bills', user_username = 'nll004')

    db.session.add(l1)
    db.session.add(l2)
    db.session.commit()

    t1 = Task(item='Wash Dishes', time_line_id='1', user_username='nll008')
    t2 = Task(item='Workout', time_line_id='1', details='Chest and legs', user_username='nll004')
    t3 = Task(item='Mow Yard', time_line_id='2', user_username='nll004')
    t4 = Task(item='Pay electric bill', list_id=2, details='Due 6/25/22', user_username='nll004')
    t5 = Task(item='Schedule dentist', time_line_id='3', details='phone# 304/538/1746', user_username='nll004')
    t6 = Task(item='Bread', list_id=1, user_username='nll004')
    t7 = Task(item='Laundry soap', list_id=1, user_username='nll004')
    t8 = Task(item='Milk', list_id=1, user_username='nll004')
    t9 = Task(item='Eggs', list_id=1, details='1.5 dozen', user_username='nll004')

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


if __name__ == '__main__':
    seed_db()
