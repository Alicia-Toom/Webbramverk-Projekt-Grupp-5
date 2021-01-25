from Controller.Utils.import_to_mongodb import import_jsons_as_books, \
    import_jsons_as_authors


def import_to_mongodb():
    folder_path = '../Models/authors_db/'
    # download_author_photo(folder_path)
    import_jsons_as_authors(folder_path)


    folder_path = '../Models/books_db/'
    # download_book_covers(folder_path)
    import_jsons_as_books(folder_path)


if __name__ == '__main__':
    import_to_mongodb()
