from Controller.authors_controller import authors
from Controller.books_controller import books
from Controller.commons import Carousel
from flask import Flask, render_template
from Controller.log_in_controller import logins
from Controller.sign_up_controller import signups
from Model.MongoDB.Models.books import Book
import os
from flask_sqlalchemy import SQLAlchemy
from Model.MySQL.DB.db_settings import SECRET_KEY


app = Flask(__name__)
app.debug = True

app.register_blueprint(books)
app.register_blueprint(authors)
app.register_blueprint(logins)
app.register_blueprint(signups)


basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "users.sql3")
app.config["SECRET_KEY"] = SECRET_KEY
db = SQLAlchemy(app)


@app.route('/')
def index():
    return render_template('index.html', carousel=Carousel(Book.all(), items_per_row=3))


if __name__ == '__main__':
    app.run()
