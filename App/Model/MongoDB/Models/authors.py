from Model.MongoDB.DB import Document, db


class Author(Document):
    collection = db.authors