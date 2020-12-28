from bson import ObjectId
from flask import Flask, render_template, send_file, make_response, abort

from Model.MongoDB.Models.books import Book

app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/books/<book_id>/cover')
def cover(book_id):
    # Example on how to use in HTML: <img src="/books/{{ book._id }}/cover" />
    book = Book.find(_id=ObjectId(book_id)).first_or_none()
    if book and book.cover_image is not None:
        cover_image = book.cover_image
        response = make_response(cover_image)
        response.headers.set('Content-Type', 'image/jpeg')
        return response
    else:
        # TODO Return default cover
        abort(404)


if __name__ == '__main__':
    app.run()
