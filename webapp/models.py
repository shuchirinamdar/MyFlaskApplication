import datetime

from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import UserMixin, AnonymousUserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import func

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String())
    password = db.Column(db.String())

    def __init__(self, username, password):
        self.username = username
        self.set_password(password)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, value):
        return check_password_hash(self.password, value)

    def is_authenticated(self):
        if isinstance(self, AnonymousUserMixin):
            return False
        else:
            return True

    def is_active(self):
        return True

    def is_anonymous(self):
        if isinstance(self, AnonymousUserMixin):
            return True
        else:
            return False

    def get_id(self):
        return self.id

    def __repr__(self):
        return '<User %r>' % self.username

class UserLog(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, user):
        self.username = user.username
        self.user_id = user.id
        self.timestamp = datetime.datetime.now()

    def add_row(self, userLog):
        db.session.add(userLog)
        db.session.commit()

    def __repr__(self):
        return "<User(name='%s', LoginTime='%s', User_Id='%s')>" % (self.username, self.timestamp, self.user_id)

class Charts(object):
    def getUserLogStats(self):
        returnList = []
        base_query = db.session.query(func.max(UserLog.username).label('username'), func.count(UserLog.id).label('total')).group_by(UserLog.user_id)
        for row in base_query.filter(UserLog.username != "").all():
            returnList.append((row.username, row.total))
        return returnList