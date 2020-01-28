import os
import pytest
from unittest.mock import MagicMock, patch
from mmbooks.book_search_query import BookSearchQuery
from mmbooks.google import Google
from mmbooks.google_book import GoogleBook
from mmbooks.google_books import GoogleBooks


class TestGoogle:
    @pytest.mark.slow
    @pytest.mark.parametrize("query", [(BookSearchQuery(isbn="9784532280208"))])
    def test_get_book(self, query):
        google_book: GoogleBook = Google().get_book(query)
        print(google_book)

    @pytest.mark.slow
    @pytest.mark.parametrize(
        "query",
        [
            (BookSearchQuery(title="カンブリア")),
            (BookSearchQuery(author="夏目漱石")),
            # (BookSearchQuery(isbn="9784532280208"))
        ],
    )
    def test_search_books(self, query):
        google_books: GoogleBooks = Google().search_books(query)
        print(google_books)

    # def test_get_request_params(self):
    #     query = BookSearchQuery()
    #     params = rakuten._get_request_params(query)
    #     assert params["applicationId"] == os.environ.get("rakuten_app_id")
    #     assert params["sort"] == "sales"
