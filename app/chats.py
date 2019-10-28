from flask import Blueprint, jsonify, request

from . import db

from .models import Message
from .models import Chat
from .models import User

ChatsApi = Blueprint('chats_api', __name__)


@ChatsApi.route('/<int:cid>/messages', methods=['POST'])
def send_message(cid):
    userid = request.args["user_id"]
    messagetext = request.json['message']
    newmessage = Message(text=messagetext, userfrom=userid, cid=cid)
    db.session.add(newmessage)
    db.session.commit()
    return jsonify(messageid=newmessage.mid, messagetext=newmessage.text), 200


#@ChatsApi.route('/<int:user_id>', methods=['GET'])
#def get_chats(user_id):
#    chats = User.chats.filter(user_id==user_id).all()
#    if chats is None:
#        return 'no chats', 404
#    return jsonify([x.to_dict() for x in chats]), 200


@ChatsApi.route('/<int:cid>/messages', methods=['GET'])
def get_chat_messages(cid):
    userid = request.args["user_id"]
    messagelist = Message.query.filter(Message.cid == cid and Message.uid == userid).all()
    if messagelist is None:
        return 'no messages', 404
    return jsonify([x.to_dict() for x in messagelist]), 200


