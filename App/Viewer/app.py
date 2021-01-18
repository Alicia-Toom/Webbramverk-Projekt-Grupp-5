from Controller.authors_controller import authors
from Controller.books_controller import books
from Controller.commons import Carousel
from flask import Flask, render_template
from Controller.log_in_controller import logins, profile, signout, error
from Controller.sign_up_controller import signups
from Model.MongoDB.Models.books import Book


app = Flask(__name__)
app.debug = True

app.register_blueprint(books)
app.register_blueprint(authors)
app.register_blueprint(logins)
app.register_blueprint(signups)
# app.register_blueprint(profile)
# app.register_blueprint(signout)
# app.register_blueprint(error)


@app.route('/')
def index():
    return render_template('index.html', carousel=Carousel(Book.all(), items_per_row=3))


if __name__ == '__main__':
    app.run()
