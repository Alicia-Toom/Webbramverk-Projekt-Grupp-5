from pymongo import MongoClient
from abc import ABC
from .db_settings import *

client = MongoClient(f"mongodb+srv://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_HOST}")
db = client.ildb


class ResultList(list):
    def first_or_none(self):
        return self[0] if len(self) > 0 else None

    def last_or_none(self):
        return self[-1] if len(self) > 0 else None


class Document(dict, ABC):
    collection = None

    def __init__(self, data):
        super().__init__()
        if '_id' not in data:
            self._id = None
        self.__dict__.update(data)

    def __repr__(self):
        return '\n'.join(f'{k} = {v}' for k, v in self.__dict__.items())

    def save(self):
        if not self._id:
            del(self.__dict__['_id'])
            return self.collection.insert_one(self.__dict__)
        else:
            return self.collection.update({'_id': self._id}, self.__dict__)

    def delete_field(self, field):
        self.collection.update({'_id': self._id}, {"$unset": {field: ""}})

    def __getitem__(self, key):
        return self.__dict__[key]

    def __setitem__(self, key, item):
        self.__dict__[key] = item

    @classmethod
    def insert_many(cls, items):
        for item in items:
            cls(item).save()

    @classmethod
    def all(cls):
        return [cls(item) for item in cls.collection.find({})]

    @classmethod
    def find(cls, **kwargs):
        return ResultList(cls(item) for item in cls.collection.find(kwargs))

    @classmethod
    def delete(cls, **kwargs):
        cls.collection.delete_many(kwargs)

    @classmethod
    def replace_document(cls, id, new_document):
        cls.collection.replace_one({'_id': id}, new_document)

    @classmethod
    def change_attribute(cls, id, attribute, value):
        cls.collection.update_one({'_id': id}, {'$set': {attribute: value}})

    @classmethod
    def push_to_embedded_list(cls, id, attribute, value):
        cls.collection.update_one({'_id': id}, {'$push': {attribute: value}})


class NestedDocument(dict):
    def init(self, data):
        self.dict.update(data)

    def repr(self):
        return self.dict.repr()
