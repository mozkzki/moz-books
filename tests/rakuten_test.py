import os
import pytest
from unittest.mock import MagicMock, patch
from mmbooks.book_search_query import BookSearchQuery
from mmbooks.rakuten import Rakuten
from mmbooks.rakuten_books import RakutenBooks


class TestRakuten:
    # @pytest.mark.parametrize(
    #     "json_str, title",
    #     [
    #         (
    #             """
    #         { "Items": [
    #                 {"Item": {"title": "hoge"}},
    #                 {"Item": {"title": "hogehoge"}}]
    #         }
    #         """,
    #             "hoge",
    #         ),
    #         ('{ "Items": []}', ""),
    #     ],
    # )
    # @patch("kbot.book.rakuten_books.RakutenBooksService._RakutenBooksService__request")
    # def test_get_one_book(self, mock_method, json_str, title):
    #     mock_method.return_value = json.loads(json_str)
    #     query = BookSearchQuery()
    #     rakuten_book = RakutenBooksService.get_one_book(query)
    #     assert mock_method.called
    #     assert rakuten_book.title == title

    @pytest.mark.slow
    @pytest.mark.parametrize(
        "query",
        [
            (BookSearchQuery(title="カンブリア")),
            (BookSearchQuery(author="夏目漱石")),
            (BookSearchQuery(isbn="9784532280208")),
        ],
    )
    def test_search_books(self, query):
        rakuten_books: RakutenBooks = Rakuten().search_books(query)
        print(rakuten_books)

    # @patch("kbot.book.rakuten_books.requests")
    # def test_request(self, mock_requests):
    #     mock_response = MagicMock()
    #     mock_response.json.return_value = ["test"]
    #     mock_requests.get.return_value = mock_response
    #     query = BookSearchQuery()
    #     json_data = RakutenBooksService._RakutenBooksService__request(query)
    #     assert mock_requests.get.called
    #     assert mock_response.json.called
    #     assert json_data == ["test"]

    def test_get_request_params(self):
        query = BookSearchQuery()
        params = Rakuten()._get_request_params(query)
        assert params["applicationId"] == os.environ.get("rakuten_app_id")
        assert params["sort"] == "sales"
