from datetime import datetime, timedelta
from app import db
from app.models import User, Post

def add_data():
    # create four users
    u1 = User(username='john', email='john@example.com')
    u2 = User(username='susan', email='susan@example.com')
    u3 = User(username='mary', email='mary@example.com')
    u4 = User(username='david', email='david@example.com')
    u5 = User(username='test_user', email='test_user@yandex.ru')
    u5.set_password('1234')
    db.session.add_all([u1, u2, u3, u4, u5])
    
    # create four posts
    now = datetime.utcnow()
    p1 = Post(body="post from john", author=u1,
                  timestamp=now + timedelta(seconds=1))
    p2 = Post(body="post from susan", author=u2,
                  timestamp=now + timedelta(seconds=4))
    p3 = Post(body="post from mary", author=u3,
                  timestamp=now + timedelta(seconds=3))
    p4 = Post(body="post from david", author=u4,
                  timestamp=now + timedelta(seconds=2))
    db.session.add_all([p1, p2, p3, p4])
    db.session.commit()
    
    u1.follow(u2)
    u1.follow(u4)
    u2.follow(u3)
    u3.follow(u4)
    u5.follow(u1)
    u5.follow(u4)
    db.session.commit()
    
    print('[okay]')
    

if __name__ == '__main__':
    add_data()
    