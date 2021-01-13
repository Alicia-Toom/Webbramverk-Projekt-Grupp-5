from flask import render_template, make_response, abort, Blueprint


signups = Blueprint('signups', __name__)


@signups.route('/signups')
def index():
    return render_template('sign_up.html')