from dataclasses import dataclass, field

from moz_books.book import Book
from moz_books.log import get_logger

LOGGER = get_logger(__name__)


@dataclass(frozen=True)
class OpenDBBook(Book):
    title: str
    author: str
    isbn: str
    publisher: str
    image_url: str
    published_date: str
    type: str = field(init=False)

    def __post_init__(self):
        # frozen=True (イミュータブル) なので self.id = value とするとエラーになる
        # 下記のようにすると回避できる
        object.__setattr__(self, "type", self.__class__.__name__)
