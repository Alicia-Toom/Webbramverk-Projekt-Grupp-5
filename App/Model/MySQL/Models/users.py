from wtforms.validators import InputRequired
from App.Model.MySQL.DB import db
from wtforms import StringField, PasswordField, BooleanField
from flask_wtf import FlaskForm


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=True)
    last_name = db.Column(db.String(100), nullable=True)
    email = db.Column(db.String(100), unique=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.VARCHAR(255))

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8)])
    remember = BooleanField('Remeber me')