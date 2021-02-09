from import_to_mongodb import import_to_mongodb
from import_to_sqlalchemy import create_users


def run_once():
    # Creates user table in SQLite, to implement a test user simply change the argument to True
    # Creates a user with username test and password test
    create_users(test=False)

    #import Books and Authors to mongodb
    import_to_mongodb()

if __name__ == '__main__':
    run_once()
