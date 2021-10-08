from dataclasses import FrozenInstanceError

import pytest
from moz_books.calil.calil_book import CalilBook


class TestCalilBook:
    def test_init(self):
        dic = self.__get_dict()
        book = CalilBook(**dic)
        assert book.isbn == "1111"
        assert book.reserveurl == "https://test.url?id=2222"
        assert book.libkey == "test-libkey"
        assert book.id == "2222"
        assert book.type == "CalilBook"

    @pytest.mark.parametrize(
        "attribute, value",
        [
            ("isbn", "new-value"),
            ("reserveurl", "new-value"),
            ("libkey", "new-value"),
            ("id", "new-value"),
            ("type", "new-value"),
            ("price", "new-value"),
        ],
    )
    def test_init_check_frozen(self, attribute, value):
        dic = self.__get_dict()
        book = CalilBook(**dic)
        with pytest.raises(FrozenInstanceError):
            setattr(book, attribute, value)

    def __get_dict(self):
        return {
            "isbn": "1111",
            "reserveurl": "https://test.url?id=2222",
            "libkey": "test-libkey",
        }
