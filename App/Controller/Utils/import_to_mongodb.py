from urllib.error import HTTPError
from Model.MongoDB.Models.authors import Author
from Model.MongoDB.Models.books import Book, BestBook, NewTitle, HotTitles
import json
import os
import urllib.request
from bson.binary import Binary
import shutil

NOT_FOUND = "../../Viewer/static/images/noimage.jpg"
#NOT_FOUND = "Model/mongoDB/Models/best_of_the_year/noimages.jpg"


def import_jsons_as_books(path):
    files = os.listdir(path)
    for file in files:
        if file.endswith(".json"):
            with open(os.path.join(path, file), encoding='utf-8') as f:
                json_data = json.load(f)

                cover_file = os.path.join(path, file.replace(".json", ".jpg"))
                if os.path.exists(cover_file):
                    with open(cover_file, "rb") as c:  # read binary
                        cover_image = Binary(c.read())  # read the data from the file
                        json_data['cover_image'] = cover_image

                #new_book = Book(json_data)
                #new_book = BestBook(json_data)
                # new_book = NewTitle(json_data)
                new_book = HotTitles(json_data)

                new_book.save()


def download_book_covers(path):
    files = os.listdir(path)  # os package
    for file in files:
        if file.endswith(".json"):
            with open(os.path.join(path, file), encoding='utf-8') as f:
                json_data = json.load(f)
                cover_url = f"http://covers.openlibrary.org/b/isbn/{json_data['ISBN']}-L.jpg?default=false"
                cover_file = os.path.join(path, file.replace(".json", ".jpg"))

                try:
                    urllib.request.urlretrieve(cover_url, cover_file)
                    print(f"Successfully downloaded cover for url: {cover_url} to file: {cover_file}")
                except HTTPError:
                    copy_file = os.path.join(path, file.replace(".json", ".jpg"))
                    shutil.copy(NOT_FOUND, copy_file)
                    print(f"Unable to download cover from url: {cover_url} to file: {cover_file}")


def import_jsons_as_authors(path):
    files = os.listdir(path)
    for file in files:
        if file.endswith(".json"):
            with open(os.path.join(path, file), encoding='utf-8') as f:
                json_data = json.load(f)

                photo_file = os.path.join(path, file.replace(".json", ".jpg"))
                if os.path.exists(photo_file):
                    with open(photo_file, "rb") as c:  # read binary
                        photo = Binary(c.read())  # read the data from the file
                        json_data['photo'] = photo

                new_author = Author(json_data)
                new_author.save()


def download_author_photo(path):
    files = os.listdir(path)  # os package
    for file in files:
        if file.endswith(".json"):
            with open(os.path.join(path, file), encoding='utf-8') as f:
                json_data = json.load(f)
                cover_url = f"http://covers.openlibrary.org/a/olid/{json_data['OLID']}-L.jpg?default=false"
                cover_file = os.path.join(path, file.replace(".json", ".jpg"))

                try:
                    urllib.request.urlretrieve(cover_url, cover_file)
                    print(f"Successfully downloaded cover for url: {cover_url} to file: {cover_file}")
                except HTTPError:
                    print(f"Unable to download cover from url: {cover_url} to file: {cover_file}")
                    copy_file = os.path.join(path, file.replace(".json", ".jpg"))
                    shutil.copy(NOT_FOUND, copy_file)



def main():
    #folder_path = '../../Model/MongoDB/Models/authors_db/'
    #download_author_photo(folder_path)
    #import_jsons_as_authors(folder_path)


    #folder_path = '../../Model/MongoDB/Models/books_db/'
    #download_book_covers(folder_path)
    #import_jsons_as_books(folder_path)


    #folder_path = '../../Model/MongoDB/Models/books_db/best_of_the_year'
    #download_book_covers(folder_path)
    #import_jsons_as_books(folder_path)

    #folder_path = '../../Model/MongoDB/Models/books_db/new_titles'
    #download_book_covers(folder_path)
    #import_jsons_as_books(folder_path)


    folder_path = '../../Model/MongoDB/Models/books_db/hot_titles'
    download_book_covers(folder_path)
    import_jsons_as_books(folder_path)


if __name__ == '__main__':
    main()
