from typing import Dict
from mmbooks.book import Book


class OpenDBBook(Book):
    def __init__(self, response_json: Dict) -> None:
        summary = response_json.get("summary", "")

        self.title = summary.get("title", "")
        self.author = summary.get("author", "")
        self.isbn = summary.get("isbn", "")
        self.publisher = summary.get("publisher", "")
        self.image_url = summary.get("cover", "")
        self.published_date = summary.get("pubdate", "")
        # self.price = response_json.get("itemPrice", "")
        # print(self)

    def to_list_string(self) -> str:
        string = "{},{},{},{},{},{}".format(
            self.__class__.__name__,
            self.isbn,
            self.title,
            self.author,
            self.publisher,
            self.published_date,
        )
        return string

    def __str__(self) -> str:
        string = """
        CLASS :     {}
        title :     {}
        author :    {}
        isbn :      {}
        publisher : {}
        cover :     {}
        pubdate:    {}
        """.format(
            self.__class__.__name__,
            self.title,
            self.author,
            self.isbn,
            self.publisher,
            self.image_url,
            self.published_date,
        )
        return string
