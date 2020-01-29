from typing import Dict
from mmbooks.book import Book
from mmbooks.books import Books
from mmbooks.service import Service
from mmbooks.book_search_query import BookSearchQuery
from mmbooks.google_book import GoogleBook
from mmbooks.google_books import GoogleBooks


class Google(Service):
    # https://developers.google.com/books/docs/v1/using
    GOOGLE_BOOKS_BASE_URL = "https://www.googleapis.com/books/v1/volumes"
    # https://www.googleapis.com/books/v1/volumes?q=isbn:9784532280208

    def __init__(self):
        super().__init__(Google.GOOGLE_BOOKS_BASE_URL)
        self._name = "google"

    def _get_books(self, response_json: Dict) -> Books:
        return GoogleBooks(response_json)
        pass

    def _get_empty_book(self) -> Book:
        return GoogleBook({})

    def _get_request_params(self, query: BookSearchQuery) -> Dict:
        query_param: Dict = query.get_dict()
        isbn = query_param.get("isbn", "")
        title = query_param.get("title", "")
        author = query_param.get("author", "")

        query_string = ""
        if isbn is not "" and isbn is not None:
            query_string = "isbn:" + isbn
        else:
            # q=intitle:カンブリア+inauthor:村上
            if title is not "" and title is not None:
                query_title = "intitle:" + title
                query_string = query_title
            if author is not "" and author is not None:
                query_author = "inauthor:" + author
                query_string += "+" + query_author

        param: Dict = {
            "q": query_string,
            "maxResults": str(40),
            "printType": "books",
            "langRestrict": "ja",
        }

        return param
