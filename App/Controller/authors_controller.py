from bson import ObjectId
from flask import render_template, Blueprint, make_response, abort
from Model.MongoDB.Models.authors import Author
from Model.MongoDB.Models.books import Book
from Controller.commons import Carousel, DataIndex

authors = Blueprint('authors', __name__)


@authors.route('/authors')
def index():
    return render_template('authors/index.html', authors_index=DataIndex(Author.all(), bucket_key_attribute='name'))


@authors.route('/authors/<author_id>')
def author(author_id):
    author = Author.find(_id=ObjectId(author_id)).first_or_none()
    books = Book.find(authors=author.name)
    return render_template('authors/author.html', author=author, carousel=Carousel(books), items_per_row=3)


@authors.route('/authors/<author_id>/photo')
def cover(author_id):
    author = Author.find(_id=ObjectId(author_id)).first_or_none()
    if author is not None and author.photo is not None:
        photo_image = author.photo
        response = make_response(photo_image)
        response.headers.set('Content-Type', 'image/jpeg')
        return response
    else:
        abort(404)