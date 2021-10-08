from typing import Dict
from moz_books.log import get_logger


LOGGER = get_logger(__name__)


class SearchParams:
    def __init__(self, title: str = "", author: str = "", isbn: str = "") -> None:
        self._title = title
        self._author = author
        self._isbn = isbn

    @property
    def title(self) -> str:
        return self._title

    @property
    def author(self) -> str:
        return self._author

    @property
    def isbn(self) -> str:
        return self._isbn

    def get_dict(self) -> Dict:
        data: Dict = {}
        if self._title != "":
            data["title"] = self._title
            LOGGER.info("search by title. value={}".format(self._title))
        if self._author != "":
            data["author"] = self._author
            LOGGER.info("search by author value={}".format(self._author))
        if self._isbn != "":
            data["isbn"] = self._isbn
            LOGGER.info("search by isbn value={}".format(self._isbn))
        return data
