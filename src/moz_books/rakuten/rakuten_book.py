from dataclasses import dataclass, field

from moz_books.book import Book


@dataclass(frozen=True)
class RakutenBook(Book):
    title: str
    author: str
    isbn: str
    caption: str
    price: str
    image_url: str
    info_url: str
    publisher: str
    published_date: str
    type: str = field(init=False)

    def __post_init__(self):
        # frozen=True (イミュータブル) なので self.id = value とするとエラーになる
        # 下記のようにすると回避できる
        object.__setattr__(self, "type", self.__class__.__name__)
