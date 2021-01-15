from random import shuffle
from bson import ObjectId
from flask import render_template, make_response, abort, Blueprint
from Model.MongoDB.Models.books import Book

books = Blueprint('books', __name__)


@books.route('/books')
def index():
    books = Book.all()
    return render_template('books/index.html', books=books)


@books.route('/books/<book_id>')
def book(book_id):
    book = Book.find(_id=ObjectId(book_id)).first_or_none()
    rec_books = []
    books = Book.find(genres=book.genres[0])
    for _ in books:
        if _['_id'] not in rec_books and _['_id'] != book['_id']:
            rec_books.append(_)
    shuffle(rec_books)

    return render_template('books/book.html', book=book)


@books.route('/books/<book_id>/cover')
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
