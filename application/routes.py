from flask import current_app as app
from .models import User
from flask import request
from flask import render_template
from .forms import LoginForm

from .chats import ChatsApi

from flask_login import current_user, login_user
from flask_login import logout_user
from flask_login import login_required


app.register_blueprint(ChatsApi, url_prefix='/api/chats')

# @app.route('/login')
# def login():
#     form = LoginForm()
#     return render_template('login.html', title='Sign In', form=form)

# @app.route('/', methods=['GET'])
# def index():
#     userid = request.args["user_id"]
#     myuser = User.query.filter(User.uid == userid).first()
#     username = myuser.username
#     return render_template('index.html', user=username)

@app.route('/chat', methods=['GET'])
def chat():
    userid = request.args["user_id"]
    myuser = User.query.filter(User.uid == userid).first()
    chatlist = [c.chat for c in myuser.chats]
    return render_template('chats.html', chats=chatlist, user_id=userid)

@app.route('/index')
@login_required
def index():
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('index.html', title='Home')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))