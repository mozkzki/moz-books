from typing import List
from unittest import mock

import pytest
from moz_books.calil.calil_book import CalilBook
from moz_books.calil.calil_service import CalilService
from moz_books.exception import InvalidSearchParamsError
from moz_books.log import get_logger
from moz_books.search_params import SearchParams
from tests.ut.moz_books.mock_response import (
    calil_one_books_response,
    calil_one_books_response_with_continue1,
    calil_one_books_response_with_continue2,
    calil_zero_books_response,
)

LOGGER = get_logger(__name__)


class TestCalilService:
    @pytest.fixture()
    def service(self) -> CalilService:
        return CalilService()

    @pytest.mark.parametrize(
        "params, expected",
        [
            (SearchParams(isbn="1111"), "isbn=1111"),
        ],
    )
    def test_search_books(self, params: SearchParams, expected: str, service: CalilService):
        with mock.patch("moz_books.service.requests") as mock_requests:
            mock_response = mock.Mock()
            mock_requests.get.return_value = mock_response
            mock_response.json.return_value = calil_one_books_response("OK")

            books: List[CalilBook] = service.search_books(params)
            for book in books:
                LOGGER.debug(book)

            mock_requests.get.assert_called_once_with(
                CalilService.CALIL_BASE_URL,
                params=f"{expected}&appkey=dummy&format=json&callback=no&systemid1=Tokyo_Nerima&systemid2=Special_Jil&systemid=Tokyo_Nerima,Special_Jil",  # noqa E501
            )
            assert len(books) == 1
            assert books[0].isbn == "1111"
            assert books[0].reserveurl == "https://test.url?BID=2222"
            assert books[0].libkey == {"Place1": "貸出可"}
            assert books[0].id == "2222"
            assert books[0].type == "CalilBook"

    def test_search_books_検索キー指定なし(self, service: CalilService):
        with mock.patch("moz_books.service.requests") as mock_requests:
            params = SearchParams()  # 検索キー何も指定なし
            # isbnを指定しないクエリはエラーになる
            with pytest.raises(InvalidSearchParamsError, match="Must specify isbn."):
                books: List[CalilBook] = service.search_books(params)
                assert len(books) == 0
                mock_requests.get.assert_not_called()

    def test_search_books_0件取得(self, service: CalilService):
        with mock.patch("moz_books.service.requests") as mock_requests:
            mock_response = mock.Mock()
            mock_requests.get.return_value = mock_response
            mock_response.json.return_value = calil_zero_books_response()

            params = SearchParams(isbn="1111")
            books: List[CalilBook] = service.search_books(params)
            assert len(books) == 0

    def test_search_books_1回目のレスポンスでcontinueが1の場合(self, service: CalilService):
        with mock.patch("moz_books.service.requests") as mock_requests:
            with mock.patch("moz_books.calil.calil_service.requests") as mock_calil_requests:
                mock_first_response = mock.Mock()
                mock_requests.get.return_value = mock_first_response
                mock_first_response.json.return_value = calil_one_books_response_with_continue1(
                    "OK"
                )
                mock_second_response = mock.MagicMock()[9:-2]
                mock_calil_requests.get.return_value = mock_second_response
                mock_second_response.text.__getitem__.return_value = (
                    calil_one_books_response_with_continue2("OK")
                )

                params = SearchParams(isbn="1111")
                books: List[CalilBook] = service.search_books(params)
                for book in books:
                    LOGGER.debug(book)

                mock_requests.get.assert_called_once_with(
                    CalilService.CALIL_BASE_URL,
                    params=f"isbn=1111&appkey=dummy&format=json&callback=no&systemid1=Tokyo_Nerima&systemid2=Special_Jil&systemid=Tokyo_Nerima,Special_Jil",  # noqa E501
                )
                assert len(books) == 1
                assert books[0].isbn == "1111"
