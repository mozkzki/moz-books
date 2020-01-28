from typing import Dict
from mmbooks.book import Book


class GoogleBook(Book):
    def __init__(self, response_json: Dict) -> None:
        volume_info = response_json.get("volumeInfo", "")

        self.title = volume_info.get("title", "")
        # 複数人あり
        # TODO: 無い場合もあるようだ
        try:
            self.author = volume_info.get("authors", "")[0]
        except Exception as e:
            self.author = ""
            print(e)
        # TODO: type==OTHERの場合は、identifierが1つしか無いため対処必要
        try:
            self.isbn = volume_info.get("industryIdentifiers", "")[1].get("identifier", "")
            self.isbn10 = volume_info.get("industryIdentifiers", "")[0].get("identifier", "")
        except Exception as e:
            # それでも無い場合あり
            try:
                self.isbn = volume_info.get("industryIdentifiers", "")[0].get("identifier", "")
            except Exception as inner_error:
                print(inner_error)
                self.isbn = ""
            print(e)
        self.description = volume_info.get("description", "")
        self.page_count = volume_info.get("pageCount", "")
        self.thumbnail_url = volume_info.get("imageLinks", "").get("thumbnail", "")
        self.published_date = volume_info.get("publishedDate", "")
        # self.price = response_json.get("itemPrice", "")
        # print(self)

    def to_list_string(self) -> str:
        string = "{},{},{},{},{},{}".format(
            self.__class__.__name__,
            self.isbn,
            self.title,
            self.author,
            self.published_date,
            self.page_count,
        )
        return string

    def __str__(self) -> str:
        string = """
        CLASS :         {}
        title :         {}
        author :        {}
        isbn10 :        {}
        isbn :          {}
        description :   {}
        page_count :    {}
        thumbnail_url : {}
        published_date: {}
        """.format(
            self.__class__.__name__,
            self.title,
            self.author,
            self.isbn10,
            self.isbn,
            self.description,
            self.page_count,
            self.thumbnail_url,
            self.published_date,
        )
        return string
