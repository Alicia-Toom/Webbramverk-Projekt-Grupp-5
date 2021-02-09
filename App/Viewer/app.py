import os

from flask_sqlalchemy import SQLAlchemy

from Controller.Utils.import_to_sqlalchemy import create_users
from Controller.authors_controller import authors
from Controller.books_controller import books

from Controller.search_controller import *
from flask_bootstrap import Bootstrap
from data import *
from Model.MongoDB.Models.authors_db import *
from Model.MongoDB.Models.books_db import *

from Controller.Utils.commons import Carousel, is_authenticated
from flask import Flask, render_template
from Controller.login_controller import login
from Controller.profile_controller import profile
from Model.MongoDB.Models.books import Book
from Model.MySQL.DB import SECRET_KEY, db
from Model.MongoDB.Models.book_categories import *

app = Flask(__name__)
app.debug = True

basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir + "/../Model/MySQL/DB", "users.sql3")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = SECRET_KEY

db = SQLAlchemy()
db.init_app(app)

app.register_blueprint(books)
app.register_blueprint(authors)
app.register_blueprint(login)
app.register_blueprint(profile)
app.register_blueprint(search)


@app.context_processor
def inject_base_context():
    return dict(authenticated=is_authenticated(), tab="app")
  

Bootstrap(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    # Import test users to database - should only be run once in development environment!
    # create_users()
    return render_template(
        'index.html',
        form=form,
        message=message,
        names=names,
        boty_carousel=Carousel(Book.find_by_array('ISBN', BEST_OF_THE_YEAR)),
        hot_titles_carousel=Carousel(Book.find_by_array('ISBN', HOT_TITLES)),
        new_titles_carousel=Carousel(Book.find_by_array('ISBN', NEW_TITLES))
    )



if __name__ == '__main__':
    app.run()


