from app import db
import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'users'
    uid = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), index=True, unique=True)
    timestamp = db.Column(db.Time, index=True, default=datetime.datetime.utcnow)
    email = db.Column(db.String(128), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    chats = db.relationship("Userschat", back_populates="user")

    def to_dict(self):

        return {
            'uid'         : self.uid,
            'username': self.username
        }

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Userschat(db.Model):
    __tablename__ = 'userschat'
    ucid = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.Time,index=True, default=datetime.datetime.utcnow)
    users_uid = db.Column(db.Integer, db.ForeignKey('users.uid'))
    chats_cid = db.Column(db.Integer, db.ForeignKey('chats.cid'))
    chat = db.relationship("Chat", back_populates="users", foreign_keys=chats_cid)
    user = db.relationship("User", back_populates="chats", foreign_keys=users_uid)

    def to_dict(self):

        return {
            'ucid'        : self.ucid,
            'timestamp'   : self.timestamp,
            'uid'         : self.users_uid,
            'cid'   : self.chats_cid,
        }

class Chat(db.Model):
    __tablename__ = 'chats'
    cid = db.Column(db.Integer, primary_key = True)
    chatname = db.Column(db.String(256))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.datetime.utcnow)
    users = db.relationship("Userschat", back_populates="chat")

    def to_dict(self):

        return {
            'cid'        : self.cid,
            'chatname'    : self.chatname,
            'timestamp'   : self.timestamp,
        }

class Message(db.Model):
    __tablename__ = 'messages'
    mid = db.Column(db.Integer, primary_key = True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.datetime.utcnow)
    text = db.Column(db.String(256))
    userfrom = db.Column(db.Integer, db.ForeignKey('users.uid'))
    cid = db.Column(db.Integer, db.ForeignKey('chats.cid'))

    from_user = db.relationship('User', foreign_keys=userfrom)

    def to_dict(self):

        return {
            'mid'         : self.mid,
            'timestamp'   : self.timestamp,
            'text'        : self.text,
            'userfrom'    : self.from_user.to_dict(),
            'cid'         : self.cid
        }

def set_password(self, password):
    self.password_hash = generate_password_hash(password)

def check_password(self, password):
    return check_password_hash(self.password_hash, password)