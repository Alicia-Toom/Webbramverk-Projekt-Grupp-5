from Model.MongoDB.Models.books import Book
import json
import os


def import_jsons_as_books(path):
    # default_cover = import_default_book_cover(path)
    files = os.listdir(path)
    for file in files:
        if file.endswith(".json"):
        #if file[-5:] == '.json':
            with open(path + file, encoding='utf-8') as f:
                json_data = json.load(f)
                # json_data['cover'] = default_cover
                new_book = Book(json_data)
                new_book.save()


# def import_default_book_cover(path):
#     with open(path + 'default_cover.jpg', 'rb') as f:
#         return bytes(f.read())