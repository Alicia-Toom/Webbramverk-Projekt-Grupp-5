from App.Model.MySQL.DB import db
from Model.MySQL.Models.users import User


def add_user(user):
    db.session.add(user)
    db.session.commit()


def find_by_username(username):
    return db.session.query(User).filter(User.username == username).first()
