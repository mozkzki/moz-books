from moz_books.log import get_logger
from moz_books.opendb.opendb_book_factory import OpenDBBookFactory
from moz_books.opendb.opendb_request_params_factory import OpenDBRequestParamsFactory
from moz_books.service import Service

LOGGER = get_logger(__name__)


class OpenDBService(Service):
    # https://openbd.jp/
    OPENDB_BASE_URL = "https://api.openbd.jp/v1/get"
    # https://api.openbd.jp/v1/get?isbn=9784532280208

    def __init__(self):
        super().__init__(
            self.__class__.__name__,
            OpenDBService.OPENDB_BASE_URL,
            OpenDBBookFactory(),
            OpenDBRequestParamsFactory(),
        )
