from flask import render_template, Blueprint, request
from Model.MongoDB.Models.authors import Author
from Model.MongoDB.Models.books import Book

search = Blueprint('search', __name__)


@search.route('/search')
def index():
    return render_template('search.html')


@search.route('/search', methods=['POST'])
def do_search():
    if "books_query" in request.form:
        books_query = request.form['books_query']
        books = Book.find(title=books_query)[0]
        search_input = books_query
        return render_template('/search.html', books=books, search_input=search_input)
    else:
        authors_query = request.form['authors_query']
        authors = Author.find(name=authors_query)[0]
        search_input = authors_query
        return render_template('/search.html', authors=authors, search_input=search_input)






