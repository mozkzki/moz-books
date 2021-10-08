import pytest
from typing import Dict
from moz_books.search_params import SearchParams


@pytest.fixture
def params_1():
    return SearchParams(isbn="11111", author="夏目漱石", title="坊っちゃん")


class TestSearchParams:
    def test_init_1(self):
        params = SearchParams()
        assert params.title == ""
        assert params.author == ""
        assert params.isbn == ""

    def test_init_2(self):
        params = SearchParams(title="坊っちゃん")
        assert params.title == "坊っちゃん"
        assert params.author == ""
        assert params.isbn == ""

    def test_init_3(self, params_1: SearchParams):
        assert params_1.title == "坊っちゃん"
        assert params_1.author == "夏目漱石"
        assert params_1.isbn == "11111"

    def test_init_4(self):
        params = SearchParams(author="夏目漱石")
        assert params.title == ""
        assert params.author == "夏目漱石"
        assert params.isbn == ""

    def test_init_5(self):
        params = SearchParams(isbn="11111")
        assert params.title == ""
        assert params.author == ""
        assert params.isbn == "11111"

    def test_set_title_ignore(self):
        params = SearchParams()
        params.title == "坊っちゃん"
        assert params.title == ""

    def test_set_author_ignore(self):
        params = SearchParams()
        params.author == "夏目漱石"
        assert params.author == ""

    def test_set_isbn_ignore(self):
        params = SearchParams()
        params.isbn == "11111"
        assert params.isbn == ""

    def test_to_dict(self, params_1: SearchParams):
        dic: Dict = params_1.get_dict()
        assert dic["title"] == "坊っちゃん"
        assert dic["author"] == "夏目漱石"
        assert dic["isbn"] == "11111"
