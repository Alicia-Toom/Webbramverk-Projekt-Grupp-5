from Model.MongoDB.DB import Document, db


class Book(Document):
    collection = db.books