from moz_books.rakuten.rakuten_book_factory import RakutenBookFactory
from moz_books.rakuten.rakuten_request_params_factory import RakutenRequestParamsFactory
from moz_books.service import Service


class RakutenService(Service):
    RAKUTEN_BASE_URL = "https://app.rakuten.co.jp/services/api/BooksBook/Search/20170404"

    def __init__(self):
        super().__init__(
            self.__class__.__name__,
            RakutenService.RAKUTEN_BASE_URL,
            RakutenBookFactory(),
            RakutenRequestParamsFactory(),
        )
