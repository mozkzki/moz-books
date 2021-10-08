from typing import List
from unittest import mock

import pytest
from moz_books.exception import InvalidSearchParamsError
from moz_books.log import get_logger
from moz_books.rakuten.rakuten_book import RakutenBook
from moz_books.rakuten.rakuten_service import RakutenService
from moz_books.search_params import SearchParams
from tests.ut.moz_books.mock_response import rakuten_one_books_response, rakuten_zero_books_response

LOGGER = get_logger(__name__)


class TestRakutenService:
    @pytest.fixture()
    def service(self):
        return RakutenService()

    @pytest.mark.parametrize(
        "params, expected",
        [
            (SearchParams(isbn="9784532280208"), "isbn=9784532280208"),
            (SearchParams(title="title1"), "title=title1"),
            (SearchParams(author="author1"), "author=author1"),
        ],
    )
    def test_search_books(self, params: SearchParams, expected: str, service: RakutenService):
        with mock.patch("moz_books.service.requests") as mock_requests:
            mock_response = mock.Mock()
            mock_requests.get.return_value = mock_response
            mock_response.json.return_value = rakuten_one_books_response()

            books: List[RakutenBook] = service.search_books(params)
            for book in books:
                LOGGER.debug(book)

            mock_requests.get.assert_called_once_with(
                RakutenService.RAKUTEN_BASE_URL,
                params=f"{expected}&applicationId=dummy&sort=sales",
            )
            assert len(books) == 1
            assert books[0].title == "title1"
            assert books[0].author == "author1"
            assert books[0].isbn == "1111"
            assert books[0].caption == "caption1"
            assert books[0].price == "500"
            assert books[0].image_url == "https://hoge.com/test/big/image.png"
            assert books[0].info_url == "https://hoge.com/test/image.png"
            assert books[0].publisher == "publisher1"
            assert books[0].published_date == "2020/01/01"
            assert books[0].type == "RakutenBook"

    def test_search_books_検索キー指定なし(self, service: RakutenService):
        with mock.patch("moz_books.service.requests") as mock_requests:
            params = SearchParams()  # 検索キー何も指定なし
            with pytest.raises(InvalidSearchParamsError):
                books: List[RakutenBook] = service.search_books(params)
                assert len(books) == 0
                mock_requests.get.assert_not_called()

    def test_search_books_0件取得(self, service: RakutenService):
        with mock.patch("moz_books.service.requests") as mock_requests:
            mock_response = mock.Mock()
            mock_requests.get.return_value = mock_response
            mock_response.json.return_value = rakuten_zero_books_response()

            params = SearchParams(isbn="12345")
            books: List[RakutenBook] = service.search_books(params)
            assert len(books) == 0
