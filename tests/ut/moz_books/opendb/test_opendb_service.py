from typing import List
from unittest import mock

import pytest
from moz_books.exception.invalid_search_params_error import InvalidSearchParamsError
from moz_books.opendb.opendb_book import OpenDBBook
from moz_books.opendb.opendb_service import OpenDBService
from moz_books.log import get_logger
from moz_books.search_params import SearchParams
from tests.ut.moz_books.mock_response import (
    opendb_one_books_response,
    opendb_zero_books_response,
)

LOGGER = get_logger(__name__)


class TestOpenDBService:
    @pytest.fixture()
    def service(self):
        return OpenDBService()

    @pytest.mark.parametrize(
        "params, expected",
        [
            (SearchParams(isbn="9784532280208"), "isbn=9784532280208"),
        ],
    )
    def test_search_books(self, params: SearchParams, expected: str, service: OpenDBService):
        with mock.patch("moz_books.service.requests") as mock_requests:
            mock_response = mock.Mock()
            mock_requests.get.return_value = mock_response
            mock_response.json.return_value = opendb_one_books_response()

            books: List[OpenDBBook] = service.search_books(params)
            for book in books:
                LOGGER.debug(book)

            mock_requests.get.assert_called_once_with(
                OpenDBService.OPENDB_BASE_URL,
                params=f"{expected}",
            )
            assert len(books) == 1
            assert books[0].title == "title1"
            assert books[0].author == "author1"
            assert books[0].isbn == "1111"
            assert books[0].publisher == "publisher1"
            assert books[0].image_url == "https://cover.openbd.jp/xxxxxx.jpg"
            assert books[0].published_date == "2013-10"
            assert books[0].type == "OpenDBBook"

    @pytest.mark.parametrize(
        "params, error_message",
        [
            (SearchParams(title="title1"), "Must specify isbn."),
            (SearchParams(), "Must specify isbn or title or author of book."),
        ],
    )
    def test_search_books_検索キー指定なし(self, params, error_message, service: OpenDBService):
        with mock.patch("moz_books.service.requests") as mock_requests:
            with pytest.raises(InvalidSearchParamsError, match=error_message):
                books: List[OpenDBBook] = service.search_books(params)
                assert len(books) == 0
                mock_requests.get.assert_not_called()

    def test_search_books_0件取得(self, service: OpenDBService):
        with mock.patch("moz_books.service.requests") as mock_requests:
            mock_response = mock.Mock()
            mock_requests.get.return_value = mock_response
            mock_response.json.return_value = opendb_zero_books_response()

            params = SearchParams(isbn="12345")
            books: List[OpenDBBook] = service.search_books(params)
            assert len(books) == 0
