from App.Model.MySQL.DB import db
from Model.MySQL.Models.users import User


def add_user(user):
    db.session.add(user)
    db.session.commit()


def find_by_username(username):
    return db.session.query(User).filter(User.username == username).first()

def update_user(user, new_values):
    success = False
    try:
        for value in new_values:
            for user_attribute, old_value in vars(user).items():


    return success

    def update_product(product: SparePart, attribute_name, new_value):
        success = False
        try:
            for product_attribute, value in vars(product).items():
                if product_attribute == attribute_name:
                    product.__setattr__(product_attribute, new_value)
            session.commit()
            success = True
        except:
            session.rollback()
        finally:
            return success