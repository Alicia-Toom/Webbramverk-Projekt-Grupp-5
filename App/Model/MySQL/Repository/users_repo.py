from App.Model.MySQL.DB import db
from Model.MySQL.Models.users import User


def add_user(user):
    db.session.add(user)
    db.session.commit()


def find_all():
    return User.query.all()


def delete_user(username):
    success = False
    try:
        db.session.query(User).filter_by(username=username).delete()
        db.session.commit()
        success = True
    except:
        db.session.rollback()
        success = False
    finally:
        return success


def find_by_username(username):
    return db.session.query(User).filter(User.username == username).first()


def update_user():
    success = False
    try:
        db.session.commit()
        success = True
    except:
        db.session.rollback()
        success = False
    finally:
        return success
