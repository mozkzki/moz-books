from typing import Dict
from mmbooks.service import Service
from mmbooks.book import Book
from mmbooks.books import Books
from mmbooks.book_search_query import BookSearchQuery
from mmbooks.opendb_book import OpenDBBook
from mmbooks.opendb_books import OpenDBBooks


class OpenDB(Service):
    # https://openbd.jp/
    OPENDB_BASE_URL = "https://api.openbd.jp/v1/get"
    # https://api.openbd.jp/v1/get?isbn=9784532280208

    def __init__(self):
        super().__init__(OpenDB.OPENDB_BASE_URL)
        self._name = "opendb"

    def _get_books(self, response_json: Dict) -> Books:
        return OpenDBBooks(response_json)

    def _get_empty_book(self) -> Book:
        return OpenDBBook({})

    def _get_request_params(self, query: BookSearchQuery) -> Dict:
        param: Dict = query.get_dict()
        return param
