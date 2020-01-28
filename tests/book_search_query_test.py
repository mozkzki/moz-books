import pytest
from typing import Dict
from mmbooks.book_search_query import BookSearchQuery


@pytest.fixture
def query_1():
    return BookSearchQuery(isbn="11111", author="夏目漱石", title="坊っちゃん")


class TestBookSearchQuery:
    def test_init_1(self):
        query = BookSearchQuery()
        assert query.title == ""
        assert query.author == ""
        assert query.isbn == ""

    def test_init_2(self):
        query = BookSearchQuery(title="坊っちゃん")
        assert query.title == "坊っちゃん"
        assert query.author == ""
        assert query.isbn == ""

    def test_init_3(self, query_1: BookSearchQuery):
        assert query_1.title == "坊っちゃん"
        assert query_1.author == "夏目漱石"
        assert query_1.isbn == "11111"

    def test_init_4(self):
        query = BookSearchQuery(author="夏目漱石")
        assert query.title == ""
        assert query.author == "夏目漱石"
        assert query.isbn == ""

    def test_init_5(self):
        query = BookSearchQuery(isbn="11111")
        assert query.title == ""
        assert query.author == ""
        assert query.isbn == "11111"

    def test_set_title_ignore(self):
        query = BookSearchQuery()
        query.title == "坊っちゃん"
        assert query.title == ""

    def test_set_author_ignore(self):
        query = BookSearchQuery()
        query.author == "夏目漱石"
        assert query.author == ""

    def test_set_isbn_ignore(self):
        query = BookSearchQuery()
        query.isbn == "11111"
        assert query.isbn == ""

    def test_to_dict(self, query_1: BookSearchQuery):
        data: Dict = query_1.get_dict()
        assert data["title"] == "坊っちゃん"
        assert data["author"] == "夏目漱石"
        assert data["isbn"] == "11111"
