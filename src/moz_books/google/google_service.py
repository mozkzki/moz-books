from moz_books.google.google_book_factory import GoogleBookFactory
from moz_books.google.google_request_params_factory import GoogleRequestParamsFactory
from moz_books.service import Service


class GoogleService(Service):
    # https://developers.google.com/books/docs/v1/using
    GOOGLE_BOOKS_BASE_URL = "https://www.googleapis.com/books/v1/volumes"
    # https://www.googleapis.com/books/v1/volumes?q=isbn:9784532280208

    def __init__(self):
        super().__init__(
            self.__class__.__name__,
            GoogleService.GOOGLE_BOOKS_BASE_URL,
            GoogleBookFactory(),
            GoogleRequestParamsFactory(),
        )
