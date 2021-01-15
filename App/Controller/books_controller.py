from random import shuffle
from bson import ObjectId
from flask import render_template, make_response, abort, Blueprint

from Controller.commons import Carousel, DataIndex
from Model.MongoDB.Models.books import Book

books = Blueprint('books', __name__)


@books.route('/books')
def index():
    return render_template('books/index.html', books_index=DataIndex(Book.all(), bucket_key_attribute='title'))


@books.route('/books/<book_id>')
def book(book_id):
    book = Book.find(_id=ObjectId(book_id)).first_or_none()
    # rec_books = []
    # books = Book.find(genres=book.genres[0])
    # for i in range(len(books)):
    #     print()
    #     if books[i] not in rec_books and books[i]._id != book._id:
    #         rec_books.append(books[i])
    # shuffle(rec_books)
    return render_template('books/book.html', book=book)


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
