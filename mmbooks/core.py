from typing import Optional
from mmbooks.book_search_query import BookSearchQuery
from mmbooks.service import Service
from mmbooks.google import Google
from mmbooks.opendb import OpenDB
from mmbooks.rakuten import Rakuten
from mmbooks.calil import Calil
from mmbooks.book import Book
from mmbooks.books import Books
from mmbooks.book_info import BookInfo


def search_all(isbn: str) -> Book:
    book_info: BookInfo = BookInfo()

    book_google = search_by_isbn(isbn, service=Google())
    book_info.set_google_book(book_google)
    book_opendb = search_by_isbn(isbn, service=OpenDB())
    book_info.set_opendb_book(book_opendb)
    book_rakuten = search_by_isbn(isbn, service=Rakuten())
    book_info.set_rakuten_book(book_rakuten)
    book_calil = search_by_isbn(isbn, service=Calil())
    book_info.set_calil_book(book_calil)

    # book_yahoo = search_by_isbn(isbn, service=Yahoo())

    return book_info


def search_by_isbn(isbn: str, service: Service = Rakuten()) -> Optional[Book]:
    if isbn is "" or isbn is None:
        raise Exception("not specified seach isbn.")

    query = BookSearchQuery(isbn=isbn)
    books = service.search_books(query)

    book: Optional[Book] = None
    find_count = len(books.list)
    if find_count == 0:
        print("search by isbn. not found.")
    elif find_count > 1:
        Exception("search by isbn. found many books.")
    elif find_count < 0:
        Exception("search by isbn. unexpected situation.")
    else:
        book = books.list[0]
    return book


def search(title: str = "", author: str = "", service: Service = Rakuten()) -> Optional[Books]:
    if title is "" or title is None:
        if author is "" or author is None:
            raise Exception("not specified seach title or author.")

    query = BookSearchQuery(title=title, author=author)
    books = service.search_books(query)

    find_count = len(books.list)
    if find_count == 0:
        print("search by query. not found.")
    elif find_count < 0:
        Exception("search by query. unexpected situation.")
    else:
        pass
    return books
