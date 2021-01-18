from flask import render_template, make_response, abort, Blueprint, request, redirect, url_for, session
import bcrypt
from Model.MySQL.Models.users import User, LoginForm
from functools import wraps
from flask_security import RoleMixin, SQLAlchemyUserDatastore, Security
from flask_security.utils import hash_password, login_user, logout_user


logins = Blueprint('logins', __name__)
profile = Blueprint('profile', __name__)
signout = Blueprint('signin', __name__)
signout = Blueprint('signout', __name__)
error = Blueprint('error', __name__)


@logins.route('/logins')
def index():
    return render_template('log_in.html', logins=logins)


@logins.route('/logins', methods=['POST'])
def signin_post():
    username = request.form['username']
    password = request.form['password']
    user = User.query.filter_by(username=username).first()
    if user:
        if bcrypt.checkpw(str.encode(password), user.password):
            session['username'] = user.username
            return redirect(url_for('profile'))
    return render_template('error.html')


@logins.route('/signin', methods=['GET', 'POST'])
def signin():
    form = LoginForm()
    if form.validate_on_submit():
        user = user_datastore.find_user(username=form.username.data)

        if user:
            login_user(user, remember=form.remember.data)
            return redirect(url_for('profile'))
    return render_template('log_in.html', form=form)


def is_authenticated():
    return 'username' in session


def authenticated(fail_route='index'):
    def decorator(route):
        @wraps(route)
        def wrapper(*args, **kwargs):
            if is_authenticated():
                return route(*args, **kwargs)
            return redirect(url_for(fail_route))
        return wrapper
    return


@logins.route('/profile')
@authenticated()
def profile():
    user = User.query.filter_by(username=session['username']).first()
    return render_template('profile.html', username=user.first_name)


@logins.route("/signout")
def signout():
    session.clear()
    return render_template('index.html', authenticeted=is_authenticated())


@logins.route('/error')
def error():
    return render_template('error.html')
