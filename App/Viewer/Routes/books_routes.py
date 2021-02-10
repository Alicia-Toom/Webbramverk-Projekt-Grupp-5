from random import sample
from bson import ObjectId
from flask import render_template, make_response, abort, Blueprint
from Controller.Utils.commons import DataIndex, compare_strings_in_lists
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
    chosen_book = Book.find(_id=ObjectId(book_id)).first_or_none()

    matched_books = []
    for b in Book.all():
        if compare_strings_in_lists(chosen_book['genres'], b['genres']):
            if b['_id'] != chosen_book['_id']:
                matched_books.append(b)

    if len(matched_books) > 2:
        recommended_books = sample(matched_books, 3)
    else:
        recommended_books = matched_books + ([chosen_book] * (3 - len(matched_books)))

    return render_template('books/book.html', book=chosen_book, rec_books=recommended_books)


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
