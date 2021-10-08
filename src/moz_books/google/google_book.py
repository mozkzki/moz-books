from dataclasses import dataclass, field

from moz_books.book import Book


@dataclass(frozen=True)
class GoogleBook(Book):
    title: str
    author: str
    isbn: str
    isbn10: str
    description: str
    page_count: str
    image_url: str
    info_url: str
    published_date: str
    type: str = field(init=False)

    def __post_init__(self):
        # frozen=True (イミュータブル) なので self.id = value とするとエラーになる
        # 下記のようにすると回避できる
        object.__setattr__(self, "type", self.__class__.__name__)
