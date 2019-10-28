from app import db
import datetime

user_chat_association = db.Table('user_chat_association', db.Model.metadata,
    db.Column('user_id', db.Integer, db.ForeignKey('users.uid')),
    db.Column('chat_id', db.Integer, db.ForeignKey('chats.cid'))
)

class User(db.Model):
    __tablename__ = 'users'
    uid = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), index=True, unique=True)
    timestamp = db.Column(db.Time, index=True, default=datetime.datetime.utcnow)
    email = db.Column(db.String(128), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    chats = db.relationship("Chat", secondary=user_chat_association, back_populates="users")

    def to_dict(self):

        return {
            'uid'         : self.uid,
            'cid'   : self.cid,
        }

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Userschat(db.Model):
    __tablename__ = 'userschat'
    ucid = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.Time,index=True, default=datetime.datetime.utcnow)
    users_uid = db.Column(db.Integer, db.ForeignKey('users.uid'))
    chats_cid = db.Column(db.Integer, db.ForeignKey('chats.cid'))

class Chat(db.Model):
    __tablename__ = 'chats'
    cid = db.Column(db.Integer, primary_key = True)
    chatname = db.Column(db.String(256))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.datetime.utcnow)

class Message(db.Model):
    __tablename__ = 'messages'
    mid = db.Column(db.Integer, primary_key = True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.datetime.utcnow)
    text = db.Column(db.String(256))
    userfrom = db.Column(db.Integer, db.ForeignKey('users.uid'))
    cid = db.Column(db.Integer, db.ForeignKey('chats.cid'))

    def to_dict(self):

        return {
            'mid'         : self.mid,
            'text'        : self.text,
            'timestamp'   : self.timestamp,
        }

