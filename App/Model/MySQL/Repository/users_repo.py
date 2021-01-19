from App.Viewer.app import db


def find_username(user):
    return user.query.filter_by(username=user.username).first()


def add_user(user):
    db.session.add(user)
    db.session.commit()
