from Model.MongoDB.DB import Document, db


class Book(Document):
    collection = db.books


class BestBook(Document):
    collection = db.bestbooks


class NewTitle(Document):
    collection = db.newbooks
