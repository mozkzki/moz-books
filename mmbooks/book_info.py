from typing import Dict
from mmbooks.book import Book
from mmbooks.opendb_book import OpenDBBook
from mmbooks.google_book import GoogleBook
from mmbooks.rakuten_book import RakutenBook
from mmbooks.calil_book import CalilBook


class BookInfo(Book):
    def __init__(self) -> None:
        pass

    def set_google_book(self, book: GoogleBook) -> None:
        if book is not None:
            self._google_book: GoogleBook = book

    def set_opendb_book(self, book: OpenDBBook) -> None:
        if book is not None:
            self._opendb_book: OpenDBBook = book

    def set_rakuten_book(self, book: RakutenBook) -> None:
        if book is not None:
            self._rakuten_book: RakutenBook = book

    def set_calil_book(self, book: CalilBook) -> None:
        if book is not None:
            self._calil_book: CalilBook = book

    def to_list_string(self) -> str:
        string = "{},{},{},{},{},{}".format(self.__class__.__name__)
        return string

    def __str__(self) -> str:
        string = """
        title(g) :     {}
        title(o) :     {}
        title(r) :     {}
        author(g) :    {}
        author(o) :    {}
        author(r) :    {}
        発売日(g) :     {}
        発売日(o) :     {}
        発売日(r) :     {}
        image(g) :     {}
        image(o) :     {}
        image(r) :     {}
        info_url(g) :  {}
        info_url(r) :  {}
        publisher(o) : {}
        publisher(r) : {}
        price(r) :     {}
        pages(g) :     {}
        yoyaku : {}
        reserve_url : {}
        """.format(
            self._google_book.title,
            self._opendb_book.title,
            self._rakuten_book.title,
            self._google_book.author,
            self._opendb_book.author,
            self._rakuten_book.author,
            self._google_book.published_date,
            self._opendb_book.published_date,
            self._rakuten_book.published_date,
            self._google_book.image_url,
            self._opendb_book.image_url,
            self._rakuten_book.image_url,
            self._google_book.info_url,
            self._rakuten_book.info_url,
            self._opendb_book.publisher,
            self._rakuten_book.publisher,
            self._rakuten_book.price,
            self._google_book.page_count,
            self._calil_book.libkey,
            self._calil_book.reserveurl,
        )
        return string
