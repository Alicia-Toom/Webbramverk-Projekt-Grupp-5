from bson import ObjectId
from flask import render_template, make_response, abort, Blueprint
from Model.MongoDB.Models.authors import Author

authors = Blueprint('Author', __name__)


@authors.route('/authors/<author_id>')
def author(author_id):
    author = Author.find(_id=ObjectId(author_id)).first_or_none()
    return render_template('author.html', author=author)


@author.route('/author/<author_id>/photo')
def photo(author_id):
    author = Author.find(_id=ObjectId(author_id)).first_or_none()
    if author is not None and author.photo is not None:
        photo = author.photo
        response = make_response(photo)
        response.headers.set('Content-Type', 'image/jpeg')
        return response
    else:
        # TODO Return default cover
        abort(404)