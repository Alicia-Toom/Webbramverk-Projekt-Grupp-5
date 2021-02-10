from flask import Blueprint, session, render_template, request

from Controller.commons import authenticated
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
    if len(first_name) > 0:
        user.first_name = first_name
    if len(last_name) > 0:
        user.last_name = last_name
    if len(city) > 0:
        user.city = city
    if len(country) > 0:
        user.country = country
    return render_template('profile/index.html', success=update_user(), user=user)
