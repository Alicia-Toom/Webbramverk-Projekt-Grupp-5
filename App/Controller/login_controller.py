from flask import render_template, Blueprint, request, redirect, url_for, session
from Model.MySQL.Models.users import User
from Model.MySQL.Repository.users_repo import find_by_username, add_user
import bcrypt

login = Blueprint('login', __name__)


@login.context_processor
def inject_login_context():
    return dict(tab='login')


@login.route('/login')
def index():
    return render_template('login/index.html')


@login.route('/login', methods=['POST'])
def do_login():
    username = request.form['username']
    password = request.form['password']
    user = find_by_username(username)
    if user:
        if bcrypt.checkpw(str.encode(password), user.password):
            session['username'] = user.username
            return redirect(url_for('profile.index'))

    return render_template('login/error.html')


@login.route('/logout')
def logout():
    session.clear()
    return render_template('login/index.html')


@login.route('/login/signup')
def signup():
    return render_template('login/signup.html', tab='signup')


@login.route('/login/signup', methods=['POST'])
def signup_post():
    username = request.form['username']
    email = request.form['email']
    if User.query.filter_by(username=username).first() or User.query.filter_by(email=email).first():
        return render_template('login/signup.html', taken=True)
    else:
        password = request.form['password']
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(str.encode(password), salt)
        user = User(username=username, email=email, password=hashed_password)

        add_user(user)
        return redirect(url_for('login.index'))
