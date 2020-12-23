from bson import ObjectId
from flask import Flask, render_template, send_file, make_response, abort

from Model.MongoDB.Models.books import Book

app = Flask(__name__)
app.debug = True


class CarouselRow:
    def __init__(self, items):
        self.items = items

    def rows(self):
        items_per_row = 4
        return [self.items[i:i + items_per_row] for i in range(0, len(self.items), items_per_row)]


@app.route('/')
def index():
    return render_template('index.html', row=CarouselRow(Book.all()))


@app.route('/books/<book_id>')
def book(book_id):
    book = Book.find(_id=ObjectId(book_id)).first_or_none()
    return render_template('book.html', book=book)


@app.route('/books/<book_id>/cover')
def cover(book_id):
    # Example on how to use in HTML: <img src="/books/{{ book._id }}/cover" />
    book = Book.find(_id=ObjectId(book_id)).first_or_none()
    if book is not None and book.cover_image is not None:
        cover_image = book.cover_image
        response = make_response(cover_image)
        response.headers.set('Content-Type', 'image/jpeg')
        return response
    else: #remove the american gods
        # TODO Return default cover
        abort(404) #http respornse code 404=notfound


if __name__ == '__main__':
    app.run()
