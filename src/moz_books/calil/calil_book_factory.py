from typing import Dict, List, Union
import typing

from moz_books.book import Book
from moz_books.calil.calil_book import CalilBook
from moz_books.interface.i_book_factory import IBookFactory
from moz_books.exception import InvalidResponseError


class CalilBookFactory(IBookFactory):
    def create(cls, response_json: Dict) -> Book:
        dic = {
            "isbn": response_json.get("isbn", ""),
            "reserveurl": response_json.get("reserveurl", ""),
            "libkey": response_json.get("libkey", ""),
        }
        return CalilBook(**dic)

    def create_list(cls, response_json: Union[Dict, List]) -> List[Book]:
        response_json_dict: Dict = typing.cast(Dict, response_json)

        isbn = response_json_dict["isbn"]
        systemid1 = response_json_dict["systemid1"]
        reserve_info = response_json_dict.get("books", "").get(isbn).get(systemid1)

        if reserve_info:
            # TODO: 複数対応
            # reserve_info = response_json_dict.get("books", "").get(isbn).get(systemid2)
            status = reserve_info.get("status")
            if status != "OK" and status != "Cache":
                raise InvalidResponseError("Status is not OK or Cache.")

            new_reserve_info = reserve_info.copy()
            new_reserve_info["isbn"] = isbn
            books: List[Book] = []
            books.append(cls.create(new_reserve_info))
            return books
        else:
            return []
