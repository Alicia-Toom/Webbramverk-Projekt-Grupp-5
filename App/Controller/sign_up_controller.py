from flask import render_template, Blueprint, request, redirect, url_for
import bcrypt
signups = Blueprint('signups', __name__)
from Model.MySQL.Models.users import User
from Model.MySQL.Repository import users_repo


@signups.route('/signups')
def signup():
    return render_template('sign_up.html')


@signups.route('/signups', methods=['POST'])
def signup_post():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(str.encode(password), salt)
    user = User(username=username, email=email, password=hashed_password, first_name="oscar", last_name="widing")
    print()

    users_repo.add_user(user)
    return redirect(url_for('log_in.html'))
