from flask import Flask, render_template, redirect, url_for, request, Blueprint
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

from data import AUTHORS

search = Blueprint('search', __name__)

class NameForm(FlaskForm):
    name = StringField('Input', validators=[DataRequired()])
    submit = SubmitField('Submit')


def get_names(source):
    names = []
    for row in source:
        name = row['name'].lower()
        names.append(name)
    return sorted(names)


def get_author(source, id):
    for row in source:
        if id == str(row["id"]):
            name = row["name"]
            photo = row["photo"]
            id = str(id)
            return id, name, photo
    return "Unknown", "Unknown", ""


def get_id(source, name):
    for row in source:
        if name.lower() == row["name"].lower():
            id = row["id"]
            id = str(id)
            return id
    return "Unknown"



@search.route('/search', methods=['GET', 'POST'])
def index():
    names = get_names(AUTHORS)
    form = NameForm()
    message = ""
    if form.validate_on_submit():
        name = form.name.data
        if name.lower() in names:
            form.name.data = ""
            id = get_id(AUTHORS, name)
            return redirect(url_for('author', id=id))
        else:
            message = "No results"


@search.route('/search/<id>')
def author(id):
    id, name, photo = get_author(AUTHORS, id)
    if name == "Unknown":
        return render_template('404.html'), 404
    else:
        return render_template('search.html', id=id, name=name, photo=photo)

@search.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404
