from typing import Optional
from mmbooks.book_search_query import BookSearchQuery
from mmbooks.service import Service
from mmbooks.rakuten import Rakuten
from mmbooks.book import Book
from mmbooks.books import Books


def search_price(isbn: str) -> Books:
    books: Books = Books({})
    book_rakuten = search_by_isbn(isbn, service=Rakuten())
    # book_yahoo = search_by_isbn(isbn, service=Yahoo())
    if book_rakuten is not None:
        books.list.append(book_rakuten)
    return books


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
