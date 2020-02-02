from typing import Dict
from mmbooks.book import Book


class RakutenBook(Book):
    def __init__(self, response_json: Dict):
        self.title = response_json.get("title", "")
        self.author = response_json.get("author", "")
        self.isbn = response_json.get("isbn", "")
        self.caption = response_json.get("itemCaption", "")
        self.price = response_json.get("itemPrice", "")
        self.image_url = response_json.get("largeImageUrl", "")
        self.info_url = response_json.get("itemUrl", "")
        self.publisher = response_json.get("publisherName", "")
        self.published_date = response_json.get("salesDate", "")

    def to_list_string(self) -> str:
        string = "{},{},{},{},{},{}".format(
            self.__class__.__name__,
            self.isbn,
            self.title,
            self.author,
            self.price,
            self.published_date,
        )
        return string

    def __str__(self) -> str:
        string = """
        CLASS :     {}
        title :     {}
        author :    {}
        isbn :      {}
        caption :   {}
        price :     {}
        image_url:  {}
        info_url:   {}
        publisher:  {}
        sales_date: {}
        """.format(
            self.__class__.__name__,
            self.title,
            self.author,
            self.isbn,
            self.caption,
            str(self.price),
            self.image_url,
            self.info_url,
            self.publisher,
            self.published_date,
        )
        return string
