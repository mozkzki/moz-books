from dataclasses import FrozenInstanceError

import pytest
from moz_books.rakuten.rakuten_book import RakutenBook


class TestRakutenBook:
    def test_init(self):
        dic = self.__get_dict()
        book = RakutenBook(**dic)
        assert book.title == "title1"
        assert book.author == "author1"
        assert book.isbn == "1111"
        assert book.caption == "caption1"
        assert book.price == "500"
        assert book.image_url == "https://hoge.com/image/test.png"
        assert book.info_url == "https://hoge.com/info"
        assert book.publisher == "publisher1"
        assert book.published_date == "2020/01/01"
        assert book.type == "RakutenBook"

    @pytest.mark.parametrize(
        "attribute, value",
        [
            ("title", "new-value"),
            ("author", "new-value"),
            ("isbn", "new-value"),
            ("caption", "new-value"),
            ("price", "new-value"),
            ("image_url", "new-value"),
            ("info_url", "new-value"),
            ("publisher", "new-value"),
            ("published_date", "new-value"),
        ],
    )
    def test_init_check_frozen(self, attribute, value):
        dic = self.__get_dict()
        book = RakutenBook(**dic)
        with pytest.raises(FrozenInstanceError):
            setattr(book, attribute, value)

    def __get_dict(self):
        return {
            "title": "title1",
            "author": "author1",
            "isbn": "1111",
            "caption": "caption1",
            "price": "500",
            "image_url": "https://hoge.com/image/test.png",
            "info_url": "https://hoge.com/info",
            "publisher": "publisher1",
            "published_date": "2020/01/01",
        }
