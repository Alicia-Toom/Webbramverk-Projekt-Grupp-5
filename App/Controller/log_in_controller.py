from flask import render_template, make_response, abort, Blueprint


logins = Blueprint('logins', __name__)


@logins.route('/logins')
def index():
    return render_template('log_in.html', logins=logins)