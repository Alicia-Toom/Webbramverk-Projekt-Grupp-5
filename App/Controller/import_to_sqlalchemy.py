import bcrypt

from Model.MySQL.DB import db
from Model.MySQL.Models.users import User
from Model.MySQL.Repository.users_repo import add_user


def create_users(test_user):
    db.create_all()
    if test_user:
        add_user(User(username="test", password=bcrypt.hashpw(str.encode("test"), bcrypt.gensalt())))
