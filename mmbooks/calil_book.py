import os
from typing import Dict
from mmbooks.book import Book


class CalilBook(Book):
    def __init__(self, json: Dict) -> None:
        self.isbn = json.get("isbn", "")
        self.reserveurl = json.get("reserveurl", "")
        self.libkey = json.get("libkey", "")
        self.id = self.reserveurl.split("=")[-1]
        self.kbot_reserve_url = (
            "https://" + os.environ["MY_SERVER_NAME"] + "/kbot/library/reserve?book_id="
        )
        # print(self)

    def to_list_string(self) -> str:
        string = "{},{},{}".format(self.__class__.__name__, self.isbn, self.libkey)
        return string

    def __str__(self) -> str:
        string = """
        CLASS :            {}
        isbn :             {}
        reserveurl :       {}
        libkey :           {}
        id :               {}
        kbot_reserve_url : {}
        """.format(
            self.__class__.__name__,
            self.isbn,
            self.reserveurl,
            str(self.libkey),
            self.id,
            self.kbot_reserve_url,
        )
        return string
