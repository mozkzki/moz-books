import os
import json
import requests
from time import sleep
from typing import Dict
from mmbooks.book_search_query import BookSearchQuery
from mmbooks.book import Book
from mmbooks.books import Books
from mmbooks.service import Service
from mmbooks.calil_book import CalilBook
from mmbooks.calil_books import CalilBooks


class Calil(Service):
    CALIL_BASE_URL = "http://api.calil.jp/check"

    def __init__(self):
        super().__init__(Calil.CALIL_BASE_URL)
        self._name = "calil"

    def get_book(self, query: BookSearchQuery) -> Book:
        books = self.search_books(query)

        if len(books.list) <= 0:
            return self._get_empty_book()
        return books.list[0]

    def search_books(self, query: BookSearchQuery) -> Books:
        response_json = self._request(query)
        new_response_json = self._polling(response_json)

        # print("-----------------------")
        # print(response_json)
        # print(json.dumps(response_json, sort_keys=True, indent=4))
        # print("-----------------------")

        new_response_json = self._add_param(new_response_json, query)
        books = self._get_books(new_response_json)
        return books

    def _polling(self, response_json: Dict) -> Dict:
        while response_json["continue"] == 1:
            sleep(2)
            response_json = self._polling_request(response_json["session"])
        # continueが0なら(1以外なら)そのままレスポンスを戻す
        return response_json

    def _polling_request(self, session: str) -> Dict:
        response: requests.models.Response = requests.get(
            self._service_url, params={"session": session}
        )
        # status codeが200番台以外なら例外発生
        response.raise_for_status()
        # 2回目以降のレスポンスはJSONP固定になるため
        json_string = response.text[9:-2]
        response_json = json.loads(json_string)
        return response_json

    def _get_books(self, response_json: Dict) -> Books:
        return CalilBooks(response_json)

    def _get_empty_book(self) -> Book:
        return CalilBook({})

    def _get_request_params(self, query: BookSearchQuery) -> Dict:
        param: Dict = {}
        if query.isbn is "" or query.isbn is None:
            raise Exception("not specified seach isbn.")
        param["isbn"] = query.isbn
        param["appkey"] = os.environ.get("calil_app_key", "dummy")
        param["format"] = "json"
        param["callback"] = "no"
        param["systemid1"] = "Tokyo_Nerima"
        param["systemid2"] = "Special_Jil"
        param["systemid"] = param["systemid1"] + "," + param["systemid2"]

        return param

    def _add_param(self, response_json: Dict, query: BookSearchQuery) -> Dict:
        new_response_json = response_json.copy()
        new_response_json["isbn"] = query.isbn
        new_response_json["systemid1"] = "Tokyo_Nerima"
        return new_response_json
