import pytest
from moz_books.calil.calil_book_factory import CalilBookFactory
from moz_books.exception import InvalidResponseError
from tests.ut.moz_books.mock_response import (
    calil_book_response,
    calil_one_books_response,
)


class TestCalilBookFactory:
    @pytest.fixture()
    def factory(self):
        return CalilBookFactory()

    def test_create(self, factory: CalilBookFactory) -> None:
        book = factory.create(calil_book_response())
        assert book.isbn == "1111"
        assert book.reserveurl == "https://test.url?BID=2222"
        assert book.libkey == {"Place1": "貸出可"}
        assert book.id == "2222"
        assert book.type == "CalilBook"

    @pytest.mark.parametrize("status", [("OK"), ("Cache")])
    def test_create_list(self, status: str, factory: CalilBookFactory) -> None:
        books = factory.create_list(calil_one_books_response(status))
        assert books[0].isbn == "1111"
        assert books[0].reserveurl == "https://test.url?BID=2222"
        assert books[0].libkey == {"Place1": "貸出可"}
        assert books[0].id == "2222"
        assert books[0].type == "CalilBook"

    def test_create_list_error(self, factory: CalilBookFactory) -> None:
        with pytest.raises(InvalidResponseError):
            factory.create_list(calil_one_books_response("Error"))
