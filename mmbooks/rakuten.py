import os
from typing import Dict
from mmbooks.book import Book
from mmbooks.books import Books
from mmbooks.service import Service
from mmbooks.book_search_query import BookSearchQuery
from mmbooks.rakuten_book import RakutenBook
from mmbooks.rakuten_books import RakutenBooks


class Rakuten(Service):

    RAKUTEN_BASE_URL = "https://app.rakuten.co.jp/services/api/BooksBook/Search/20170404"

    def __init__(self):
        super().__init__(Rakuten.RAKUTEN_BASE_URL)
        self._name = "rakuten"

    def _get_books(self, response_json: Dict) -> Books:
        return RakutenBooks(response_json)

    def _get_empty_book(self) -> Book:
        return RakutenBook({})

    def _get_request_params(self, query: BookSearchQuery) -> Dict:
        param: Dict = query.get_dict()
        param["applicationId"] = os.environ.get("rakuten_app_id")
        param["sort"] = "sales"
        return param
