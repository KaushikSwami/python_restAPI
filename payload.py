def addbook_payload(book_name, isbn, aisle, author):
    body = {

        "name": book_name,
        "isbn": isbn,
        "aisle": aisle,
        "author": author
    }
    return body


def deletebook_payload(book):
    body = {
        "ID": book
    }
    return body
