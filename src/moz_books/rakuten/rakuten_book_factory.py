from typing import Dict, List, Union
import typing

from moz_books.book import Book
from moz_books.interface.i_book_factory import IBookFactory
from moz_books.log import get_logger
from moz_books.rakuten.rakuten_book import RakutenBook

LOGGER = get_logger(__name__)


class RakutenBookFactory(IBookFactory):
    def create(cls, response_json: Dict) -> Book:
        dic = {
            "title": response_json.get("title", ""),
            "author": response_json.get("author", ""),
            "isbn": response_json.get("isbn", ""),
            "caption": response_json.get("itemCaption", ""),
            "price": response_json.get("itemPrice", ""),
            "image_url": response_json.get("largeImageUrl", ""),
            "info_url": response_json.get("itemUrl", ""),
            "publisher": response_json.get("publisherName", ""),
            "published_date": response_json.get("salesDate", ""),
        }
        return RakutenBook(**dic)

    def create_list(cls, response_json: Union[Dict, List]) -> List[Book]:
        response_json_dict: Dict = typing.cast(Dict, response_json)
        books: List[Book] = []
        for item in response_json_dict.get("Items", ""):
            books.append(cls.create(item.get("Item")))
        LOGGER.info("found {} items.".format(len(books)))
        return books
