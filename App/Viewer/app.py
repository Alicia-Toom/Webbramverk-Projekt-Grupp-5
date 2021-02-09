import os
from flask_sqlalchemy import SQLAlchemy
from Viewer.Routes.authors_routes import authors
from Viewer.Routes.books_routes import books
from Viewer.Routes.search_routes import *
from flask_bootstrap import Bootstrap
from data import *
from Controller.Utils.commons import Carousel, is_authenticated
from flask import Flask, render_template
from Viewer.Routes.login_routes import login
from Viewer.Routes.profile_routes import profile
from Model.MongoDB.Models.books import Book
from Model.MySQL.DB import SECRET_KEY
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

Bootstrap(app)


@app.context_processor
def inject_base_context():
    return dict(authenticated=is_authenticated(), tab="app")


@app.route('/')
def index():
    return render_template(
        'index.html',
        boty_carousel=Carousel(Book.find_by_array('ISBN', BEST_OF_THE_YEAR)),
        hot_titles_carousel=Carousel(Book.find_by_array('ISBN', HOT_TITLES)),
        new_titles_carousel=Carousel(Book.find_by_array('ISBN', NEW_TITLES))
    )


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run()