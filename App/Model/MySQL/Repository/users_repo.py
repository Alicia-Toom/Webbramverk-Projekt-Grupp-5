from App.Viewer.app import db


def add_user(user):
    db.session.add(user)
    db.session.commit()
