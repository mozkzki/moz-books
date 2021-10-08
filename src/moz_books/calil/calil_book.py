from dataclasses import dataclass, field
from moz_books.book import Book


@dataclass(frozen=True)
class CalilBook(Book):
    isbn: str
    reserveurl: str
    libkey: str
    id: str = field(init=False)
    type: str = field(init=False)

    def __post_init__(self):
        # frozen=True (イミュータブル) なので self.id = value とするとエラーになる
        # 下記のようにすると回避できる
        object.__setattr__(self, "id", self.reserveurl.split("=")[-1])
        object.__setattr__(self, "type", self.__class__.__name__)
