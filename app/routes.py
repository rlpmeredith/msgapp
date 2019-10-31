from app import app
from app.models import User
from flask import request
from flask import render_template
from app.forms import LoginForm

from .chats import ChatsApi
from .models import User

app.register_blueprint(ChatsApi, url_prefix='/api/chats')

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)

@app.route('/', methods=['GET'])
def index():
    userid = request.args["user_id"]
    myuser = User.query.filter(User.uid == userid).first()
    username = myuser.username
    return render_template('index.html', user=username)

@app.route('/chat', methods=['GET'])
def chat():
    userid = request.args["user_id"]
    myuser = User.query.filter(User.uid == userid).first()
    chatlist = [c.chat for c in myuser.chats]
    return render_template('chats.html', chats=chatlist, user_id=userid)