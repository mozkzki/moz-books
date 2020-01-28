import json
import pytest
from typing import List
from mmbooks.rakuten_book import RakutenBook
from mmbooks.rakuten_books import RakutenBooks


@pytest.fixture()
def books_1():
    json_str = """
        { "Items": [
            {"Item": {"title": "hoge"}},
            {"Item": {"title": "hogehoge"}}]
        }
    """
    books = RakutenBooks(json.loads(json_str))
    return books


class TestRakutenBooks:
    def test_new(self, books_1):
        assert isinstance(books_1, RakutenBooks)
        assert len(books_1.list) == 2

    def test_new_empty(self):
        books = RakutenBooks(json.loads('{"Items": []}'))
        assert isinstance(books, RakutenBooks)
        assert len(books.list) == 0

    @pytest.mark.parametrize("index, length", [(0, 0), (1, 1)])
    def test_slice(self, books_1: RakutenBooks, index, length):
        books: List = books_1.list[0:index]
        assert len(books) == length

    def test_get(self, books_1: RakutenBooks):
        book: RakutenBook = books_1.list[0]
        assert isinstance(book, RakutenBook)
        assert book.title == "hoge"
