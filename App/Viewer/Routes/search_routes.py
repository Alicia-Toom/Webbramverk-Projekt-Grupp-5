from flask import Flask, render_template, redirect, url_for, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


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


