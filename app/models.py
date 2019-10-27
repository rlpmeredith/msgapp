from app import db

class Users(db.Model):
    uid = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(128), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Userschats(db.Model):
    ucid = db.Column(db.Integer, primary_key = True)
    timestamp = db.Column(db.Time)
    chats_cid = db.Column(db.Integer, db.ForeignKey('messages.mid'))
    users_uid = db.Column(db.Integer, db.ForeignKey('users.uid'))

class Messages(db.Model):
    mid = db.Column(db.Integer, primary_key = True)
    timestamp = db.Column(db.Time)
    text = db.Column(db.String(256))

