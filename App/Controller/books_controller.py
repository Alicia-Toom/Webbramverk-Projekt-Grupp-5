from random import shuffle
from bson import ObjectId
from flask import render_template, make_response, abort, Blueprint

from Controller.Utils.commons import DataIndex
from Model.MongoDB.Models.books import Book

books = Blueprint('books', __name__)


@books.context_processor
def inject_books_context():
    return dict(tab="books")


@books.route('/books')
def index():
    return render_template('books/index.html', books_index=DataIndex(Book.all(), bucket_key_attribute='title'))


@books.route('/books/<book_id>')
def book(book_id):
    book = Book.find(_id=ObjectId(book_id)).first_or_none()
    rec_books = []
    books = Book.find(genres=book.genres[0])
    while len(rec_books) < 4:
        for _ in books:
            if _['_id'] != book['_id']:
                rec_books.append(_)
    shuffle(rec_books)

    return render_template('books/book.html', book=book, rec_books=rec_books)


@books.route('/books/<book_id>/cover')
def cover(book_id):
    book = Book.find(_id=ObjectId(book_id)).first_or_none()
    if book is not None and book.cover_image is not None:
        cover_image = book.cover_image
        response = make_response(cover_image)
        response.headers.set('Content-Type', 'image/jpeg')
        return response
    else:
        abort(404)
