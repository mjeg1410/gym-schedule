from application import db, login_manager
from flask_login import UserMixin

class Gym(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    gym_name = db.Column(db.String(100), nullable=False, unique=True)
    postcode = db.Column(db.String(7), nullable=False, unique=True)

    def __repr__(self):
        return ''.join([
            'class_id: ', self.class_id, '\r\n',
            'activity: ', self.activity, '\r\n', 'date:', self.date, 'time: ', self.time
    ])

    def __repr__(self):
        return ''.join([
            'User: ', self.first_name, ' ', self.last_name
    ])

class Classes(db.Model):
    class_id = db.Column(db.Integer, primary_key=True)
    activity= db.Column(db.String(30), nullable=False)
    date=db.Column(db.date, nullable=False)
    time=db.Column(db.time, nullable=False) 

    def __repr__(self):
        return ''.join([
            'id: ', self.id, '\r\n',
            'gym_name: ', self.gym_name, '\r\n', 'postcode:', self.postcode
    ])

    def __repr__(self):
        return ''.join([
            'User: ', self.first_name, ' ', self.last_name
    ])

            
class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(500), nullable=False)
    posts = db.relationship('Posts', backref='author', lazy=True)

    def __repr__(self):
        return ''.join([
            'id: ', self.id, '\r\n',
            'gym_name: ', self.gym_name, '\r\n', 'postcode:', self.postcode
    ])

    def __repr__(self):
        return ''.join([
            'class_id: ', self.class_id, '\r\n',
            'activity: ', self.activity, '\r\n', 'date:', self.date, 'time: ', self.time
    ])

@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))