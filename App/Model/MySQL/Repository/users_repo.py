from App.Model.MySQL.DB import db
from Model.MySQL.Models.users import User


def add_user(user):
    db.session.add(user)
    db.session.commit()


def find_all():
    return db.User.query.order_by(id).all()


# def delete_user(username):
#     success = False
#     try:
#         db.
#         db.session



def find_by_username(username):
    return db.session.query(User).filter(username == username).first()


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

