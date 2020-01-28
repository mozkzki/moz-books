from typing import Dict, List
from mmbooks.book import Book
from mmbooks.books import Books
from mmbooks.google_book import GoogleBook


class GoogleBooks(Books):
    def __init__(self, response_json: Dict) -> None:
        super().__init__(response_json)

    def _get_book_list(self, response_json: Dict) -> List[Book]:
        total_count = int(response_json.get("totalItems", ""))
        print("found {} items.".format(total_count))

        books: List = []
        for item in response_json.get("items", ""):
            # print(">>>>>>>>>")
            # print(item)
            # print(">>>>>>>>>")
            books.append(GoogleBook(item))
        return books
