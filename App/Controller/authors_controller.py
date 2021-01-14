from flask import render_template,  Blueprint
from Model.MongoDB.Models.authors import Author

authors = Blueprint('authors', __name__)


@authors.route('/authors')
def index():
    authors = Author.all()
    return render_template('authors/index.html', authors=authors)