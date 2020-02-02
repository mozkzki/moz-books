import requests
import json
from typing import Dict
from dotenv import load_dotenv
from mmbooks.book import Book
from mmbooks.books import Books
from mmbooks.book_search_query import BookSearchQuery


class Service:
    def __init__(self, service_url: str) -> None:
        load_dotenv(verbose=True)
        self._service_url = service_url
        self._name = "default"

    def get_book(self, query: BookSearchQuery) -> Book:
        books = self.search_books(query)

        if len(books.list) <= 0:
            return self._get_empty_book()
        return books.list[0]

    def search_books(self, query: BookSearchQuery) -> Books:
        response_json = self._request(query)

        # print("-----------------------")
        # print(response_json)
        # print(json.dumps(response_json, sort_keys=True, indent=4))
        # print("-----------------------")

        return self._get_books(response_json)

    def _request(self, query: BookSearchQuery) -> Dict:
        response: requests.models.Response = requests.get(
            self._service_url, params=self._get_request_params(query)
        )
        # status codeが200番台以外なら例外発生
        response.raise_for_status()
        response_json = response.json()
        return response_json

    # 要オーバーライド
    def _get_books(self, response_json: Dict) -> Books:
        pass

    # 要オーバーライド
    def _get_empty_book(self) -> Book:
        pass

    # 要オーバーライド
    def _get_request_params(self, query: BookSearchQuery) -> Dict:
        pass

    @property
    def name(self) -> str:
        return self._name
