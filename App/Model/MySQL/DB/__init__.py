import os
from flask_sqlalchemy import SQLAlchemy
from App.Viewer.app import app
from Model.MySQL.DB.db_settings import SECRET_KEY

basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "users.sql3")
app.config["SECRET_KEY"] = SECRET_KEY
db = SQLAlchemy(app)
