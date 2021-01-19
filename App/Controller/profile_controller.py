from flask import Blueprint, session, render_template

from Controller.Utils.commons import authenticated
from Model.MySQL.Repository.users_repo import find_by_username

profile = Blueprint('profile', __name__)


@profile.context_processor
def inject_profile_context():
    return dict(tab="profile")


@profile.route('/profile')
@authenticated()
def index():
    user = find_by_username(session['username'])
    return render_template('profile/index.html', user=user)
