from Controller.books_controller import books
from Controller.commons import Carousel
from flask import Flask, render_template

from Model.MongoDB.Models.books import Book

app = Flask(__name__)
app.debug = True

app.register_blueprint(books)


@app.route('/')
def index():
    return render_template('index.html', carousel=Carousel(Book.all(), items_per_row=3))


if __name__ == '__main__':
    app.run()
