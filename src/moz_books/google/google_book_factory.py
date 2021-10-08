from typing import Dict, List, Union
import typing

from moz_books.book import Book
from moz_books.exception import InvalidResponseError
from moz_books.google.google_book import GoogleBook
from moz_books.interface.i_book_factory import IBookFactory
from moz_books.log import get_logger

LOGGER = get_logger(__name__)


class GoogleBookFactory(IBookFactory):
    def create(cls, response_json: Dict) -> Book:
        volume_info = response_json.get("volumeInfo", "")

        author = isbn = isbn10 = ""

        # 複数人あり
        # TODO: 無い場合もあるようだ
        try:
            author = volume_info.get("authors")[0]
        except Exception as e:
            LOGGER.warning("failed to get author. error={}".format(e))
            author = "UNKNOWN"
        # TODO: type==OTHERの場合は、identifierが1つしか無いため対処必要
        try:
            isbn = volume_info.get("industryIdentifiers", "")[1].get("identifier", "")
            isbn10 = volume_info.get("industryIdentifiers", "")[0].get("identifier", "")
        except Exception as e:
            print("failed to get isbn13. error={}".format(e))
            # それでも無い場合あり
            try:
                isbn = volume_info.get("industryIdentifiers", "")[0].get("identifier", "")
            except Exception as inner_error:
                LOGGER.warning("failed to get isbn10. error={}".format(inner_error))
                raise InvalidResponseError()

        dic = {
            "author": author,
            "isbn": isbn,
            "isbn10": isbn10,
            "title": volume_info.get("title", ""),
            "description": volume_info.get("description", ""),
            "page_count": volume_info.get("pageCount", ""),
            "image_url": volume_info.get("imageLinks", {"thumbnail": ""}).get("thumbnail", ""),
            "info_url": volume_info.get("infoLink", ""),
            "published_date": volume_info.get("publishedDate", ""),
        }
        return GoogleBook(**dic)

    def create_list(cls, response_json: Union[Dict, List]) -> List[Book]:
        response_json_dict: Dict = typing.cast(Dict, response_json)
        total_count = int(response_json_dict.get("totalItems", ""))
        LOGGER.info("totalItems is {} items.".format(total_count))

        books: List[Book] = []
        for item in response_json_dict.get("items", ""):
            books.append(cls.create(item))
        LOGGER.info("found {} items.".format(len(books)))
        return books
