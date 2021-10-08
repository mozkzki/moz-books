from typing import Dict, List, Union
import typing

from moz_books.log import get_logger
from moz_books.book import Book
from moz_books.interface.i_book_factory import IBookFactory
from moz_books.opendb.opendb_book import OpenDBBook

LOGGER = get_logger(__name__)


class OpenDBBookFactory(IBookFactory):
    def create(cls, response_json: Dict) -> Book:
        summary = response_json.get("summary", "")

        dic = {
            "title": summary.get("title", ""),
            "author": summary.get("author", ""),
            "isbn": summary.get("isbn", ""),
            "publisher": summary.get("publisher", ""),
            "image_url": summary.get("cover", ""),
            "published_date": summary.get("pubdate", ""),
            # TODO: response_json.get("itemPrice", "")
        }
        return OpenDBBook(**dic)

    def create_list(cls, response_json: Union[Dict, List]) -> List[Book]:
        response_json_list: List = typing.cast(List, response_json)
        books: List[Book] = []
        for item in response_json_list:
            if item:
                books.append(cls.create(item))
        LOGGER.info("found {} items.".format(len(books)))
        return books
