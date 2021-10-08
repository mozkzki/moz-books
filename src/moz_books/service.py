import json
from typing import Dict, List

import requests
from dotenv import load_dotenv

from moz_books.book import Book
from moz_books.exception.invalid_search_params_error import InvalidSearchParamsError
from moz_books.interface.i_book_factory import IBookFactory
from moz_books.interface.i_request_params_factory import IRequestParamsFactory
from moz_books.interface.i_service import IService
from moz_books.log import get_logger
from moz_books.search_params import SearchParams

LOGGER = get_logger(__name__)


class Service(IService):
    def __init__(
        self,
        name: str,
        url: str,
        book_factory: IBookFactory,
        request_factory: IRequestParamsFactory,
    ) -> None:
        load_dotenv(verbose=True)
        self.__url = url
        self.__name = name
        self._book_factory = book_factory  # protected
        self.__request_factory = request_factory

    def search_books(self, params: SearchParams) -> List[Book]:
        books: List[Book] = []

        if not params.isbn and not params.title and not params.author:
            LOGGER.error("search params: {}".format(params.get_dict()))
            raise InvalidSearchParamsError("Must specify isbn or title or author of book.")

        response_json = self._request(params)
        LOGGER.debug(json.dumps(response_json, sort_keys=True, indent=4))
        books = self._book_factory.create_list(response_json)

        count = len(books)
        if count == 0:
            LOGGER.warning("no such books.")
            return []

        return books

    def _request(self, query: SearchParams) -> Dict:
        params_str, _ = self.__request_factory.create(query)
        response: requests.models.Response = requests.get(
            self.__url,
            params=params_str,
        )
        # status codeが200番台以外なら例外発生
        response.raise_for_status()
        response_json = response.json()
        return response_json
