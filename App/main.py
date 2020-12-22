from Controller.import_to_db_from_json import import_jsons_as_books, import_jsons_as_authors, \
    download_book_covers


def main():
    folder_path = 'Model/MongoDB/Models/authors_db/'
    #import_jsons_as_authors(folder_path)

    folder_path = 'Model/MongoDB/Models/books_db/'
    #download_book_covers(folder_path)
    import_jsons_as_books(folder_path)

if __name__ == '__main__':
    main()
