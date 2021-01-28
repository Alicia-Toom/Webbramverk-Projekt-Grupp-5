from flask import Blueprint, session, render_template, request

from Controller.Utils.commons import authenticated
from Model.MySQL.Repository.users_repo import find_by_username, update_user

profile = Blueprint('profile', __name__)


@profile.context_processor
def inject_profile_context():
    return dict(tab="profile")


@profile.route('/profile')
@authenticated()
def index():
    user = find_by_username(session['username'])
    return render_template('profile/index.html', user=user)


@profile.route('/profile', methods=['POST'])
@authenticated()
def index_post():
    user = find_by_username(session['username'])
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    city = request.form['city']
    country = request.form['country']
    print()
    new_values = []
    if first_name:
        new_values.append(first_name)
    if last_name:
        new_values.append(last_name)
    if city:
        new_values.append(city)
    if country:
        new_values.append(country)
    return render_template('profile/index.html', user=user, sucess=update_user(user, new_values))
