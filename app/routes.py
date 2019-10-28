from app import app
from app.models import User

from .chats import ChatsApi

app.register_blueprint(ChatsApi, url_prefix='/api/chats')

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


