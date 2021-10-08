from typing import List
from unittest import mock

import pytest
from moz_books.exception import InvalidSearchParamsError
from moz_books.google.google_book import GoogleBook
from moz_books.google.google_service import GoogleService
from moz_books.log import get_logger
from moz_books.search_params import SearchParams
from tests.ut.moz_books.mock_response import google_empty_books_response, google_one_books_response

LOGGER = get_logger(__name__)


class TestGoogleService:
    @pytest.fixture()
    def service(self):
        return GoogleService()

    @pytest.mark.parametrize(
        "params, expected",
        [
            (SearchParams(isbn="9784532280208"), "isbn:9784532280208"),
            (SearchParams(title="title1"), "intitle:title1"),
            (SearchParams(author="author1"), "inauthor:author1"),
        ],
    )
    def test_search_books(self, params: SearchParams, expected: str, service: GoogleService):
        with mock.patch("moz_books.service.requests") as mock_requests:
            mock_response = mock.Mock()
            mock_requests.get.return_value = mock_response
            mock_response.json.return_value = google_one_books_response()

            books: List[GoogleBook] = service.search_books(params)
            for book in books:
                LOGGER.debug(book)

            mock_requests.get.assert_called_once_with(
                GoogleService.GOOGLE_BOOKS_BASE_URL,
                params=f"q={expected}&maxResults=40&printType=books",
            )
            assert len(books) == 1
            assert books[0].author == "author1"
            assert books[0].description == "description1"
            assert books[0].image_url == "http://books.google.com/books/content?id=xxxxx"
            assert books[0].info_url == "http://books.google.co.jp/books?id=yyyyyy"
            assert books[0].isbn == "9784532280208"
            assert books[0].isbn10 == "4532280206"
            assert books[0].page_count == 284
            assert books[0].published_date == "2013-10"
            assert books[0].title == "title1"
            assert books[0].type == "GoogleBook"

    def test_search_books_検索キー指定なし(self, service: GoogleService):
        with mock.patch("moz_books.service.requests") as mock_requests:
            params = SearchParams()  # 検索キー何も指定なし
            with pytest.raises(InvalidSearchParamsError):
                books: List[GoogleBook] = service.search_books(params)
                assert len(books) == 0
                mock_requests.get.assert_not_called()

    def test_search_books_0件取得(self, service: GoogleService):
        with mock.patch("moz_books.service.requests") as mock_requests:
            mock_response = mock.Mock()
            mock_requests.get.return_value = mock_response
            mock_response.json.return_value = google_empty_books_response()

            params = SearchParams(isbn="12345")
            books: List[GoogleBook] = service.search_books(params)
            assert len(books) == 0
