from flask import Blueprint, jsonify, request

from . import db

from .models import Message
from .models import Chat
from .models import User
from .models import Userschat


ChatsApi = Blueprint('chats_api', __name__)


@ChatsApi.route('/<int:cid>/messages', methods=['POST'])
def send_message(cid):
    userid = request.args["user_id"]
    messagetext = request.json['message']
    newmessage = Message(text=messagetext, userfrom=userid, cid=cid)
    db.session.add(newmessage)
    db.session.commit()
    return jsonify(newmessage.to_dict()), 200


@ChatsApi.route('/<int:user_id>', methods=['GET'])
def get_chats(user_id):
    myuser = User.query.filter(User.uid == user_id).first()
    chatlist = [c.chat for c in myuser.chats]
#    chatlist = myuser.chats

    return jsonify([x.to_dict() for x in chatlist]), 200


@ChatsApi.route('/<int:cid>/messages', methods=['GET'])
def get_chat_messages(cid):
    userid = request.args["user_id"]
    messagelist = Message.query.filter(Message.cid == cid).all()
    if messagelist is None:
        return 'no messages', 404
    return jsonify([x.to_dict() for x in messagelist]), 200