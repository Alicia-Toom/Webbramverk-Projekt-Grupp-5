from Controller.import_to_db_from_json import import_jsons_as_books, import_jsons_as_authors


def main():
    folder_path = 'Model/MongoDB/Models/authors_db/'
    import_jsons_as_authors(folder_path)


if __name__ == '__main__':
    main()
