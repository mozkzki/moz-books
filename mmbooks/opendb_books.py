from typing import Dict, List
from mmbooks.book import Book
from mmbooks.books import Books
from mmbooks.opendb_book import OpenDBBook


class OpenDBBooks(Books):
    def __init__(self, response_json: Dict) -> None:
        super().__init__(response_json)

    def _get_book_list(self, response_json: List) -> List[Book]:
        total_count = len(response_json)
        print("found {} items.".format(total_count))
        if total_count == 1 and response_json[0] is None:
            print("but countents is empty.")
            return []

        books: List = []
        for item in response_json:
            # print(">>>>>>>>>")
            # print(item)
            # print(">>>>>>>>>")
            books.append(OpenDBBook(item))
        return books
