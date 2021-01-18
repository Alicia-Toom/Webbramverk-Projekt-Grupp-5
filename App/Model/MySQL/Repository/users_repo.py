from App.Model.MySQL.DB import db


def add_user(user):
    db.session.add(user)
    db.session.commit()
