from flask import Flask, render_template, redirect, url_for, request, Blueprint, session, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from data import AUTHORS

from Model.MongoDB.Models.authors import Author
from Model.MongoDB.Models.books import Book

search = Blueprint('search', __name__)

# class NameForm(FlaskForm):
#     name = StringField('Input', validators=[DataRequired()])
#     submit = SubmitField('Submit')
#
#
# def get_names(source):
#     names = []
#     for row in source:
#         name = row['name'].lower()
#         names.append(name)
#     return sorted(names)
#
#
# def get_author(source, id):
#     for row in source:
#         if id == str(row["id"]):
#             name = row["name"]
#             photo = row["photo"]
#             id = str(id)
#             return id, name, photo
#     return "Unknown", "Unknown", ""
#
#
# def get_id(source, name):
#     for row in source:
#         if name.lower() == row["name"].lower():
#             id = row["id"]
#             id = str(id)
#             return id
#     return "Unknown"


@search.route('/search')
def index():
    return render_template('search.html')


@search.route('/search', methods=['POST'])
def do_search():
    if "books_query" in request.form:
        books_query = request.form['books_query']
        books = Book.find(title=books_query)
        return render_template('/search.html', books=books)

    else:
        authors_query =request.form['authors_query']
        authors = Author.find(name=authors_query)
        return render_template('/search.html', authors=authors)

