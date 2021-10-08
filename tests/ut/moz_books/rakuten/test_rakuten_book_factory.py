import pytest
from moz_books.rakuten.rakuten_book import RakutenBook
from moz_books.rakuten.rakuten_book_factory import RakutenBookFactory
from tests.ut.moz_books.mock_response import (
    rakuten_book_response,
    rakuten_two_books_response,
)


class TestRakutenBookFactory:
    @pytest.fixture()
    def factory(self):
        return RakutenBookFactory()

    def test_create(self, factory: RakutenBookFactory) -> None:
        dic = rakuten_book_response("title1")
        book: RakutenBook = factory.create(dic)
        assert book.title == "title1"
        assert book.author == "author1"
        assert book.isbn == "1111"
        assert book.caption == "caption1"
        assert book.price == "500"
        assert book.image_url == "https://hoge.com/test/big/image.png"
        assert book.info_url == "https://hoge.com/test/image.png"
        assert book.publisher == "publisher1"
        assert book.published_date == "2020/01/01"
        assert book.type == "RakutenBook"

    def test_create_list(self, factory: RakutenBookFactory) -> None:
        books = factory.create_list(rakuten_two_books_response())
        assert books[0].title == "title1"
        assert books[1].title == "title2"

    @pytest.mark.parametrize("response", [({"Items": []}), ({})])
    def test_create_list_empty(self, response, factory: RakutenBookFactory) -> None:
        books = factory.create_list(response)
        assert len(books) == 0
