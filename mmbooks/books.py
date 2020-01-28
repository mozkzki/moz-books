from typing import List, Dict

# from mmbooks.rakuten_books import RakutenBooks
# from mmbooks.calil_book import CalilBook
from mmbooks.book import Book


class Books:
    def __init__(self, response_json: Dict) -> None:
        self._list: List[Book] = self._get_book_list(response_json)

    # 要オーバーライド
    def _get_book_list(self, response_json: Dict) -> List[Book]:
        return []

    def __str__(self) -> str:
        string = ""
        for book in self._list:
            string += "\n{}".format(book.to_list_string())
        return string

    @property
    def list(self) -> List[Book]:
        return self._list
