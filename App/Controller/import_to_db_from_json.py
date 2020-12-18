from Model.MongoDB.Models.books import Book
import json
import os


def import_jsons_as_books(path):
    files = os.listdir(path)
    for file in files:
        if file[-5:] == '.json':
            with open(path + file, encoding='utf-8') as f:
                json_data = json.load(f)
                new_book = Book(json_data)
                new_book.save()
