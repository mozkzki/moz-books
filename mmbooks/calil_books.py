from typing import Dict, List
from mmbooks.book import Book
from mmbooks.books import Books
from mmbooks.calil_book import CalilBook


class CalilBooks(Books):
    def __init__(self, response_json: Dict) -> None:
        super().__init__(response_json)

    def _get_book_list(self, response_json: Dict) -> List[Book]:
        isbn = response_json["isbn"]
        systemid1 = response_json["systemid1"]

        reserve_info = response_json.get("books", "").get(isbn).get(systemid1)
        # reserve_info = response_json.get("books", "").get(isbn).get(systemid2)
        status = reserve_info.get("status")
        if status != "OK" and status != "Cache":
            return [CalilBook({})]

        # TODO: 個数表示
        # total_count = int(response_json.get("totalItems", ""))
        # print("found {} items.".format(total_count))

        books: List = []
        # TODO: 複数対応
        # books.append(CalilBook(isbn, reserve_info))
        new_reserve_info = reserve_info.copy()
        new_reserve_info["isbn"] = isbn
        books.append(CalilBook(new_reserve_info))
        return books
