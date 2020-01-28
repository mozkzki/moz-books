from typing import Dict


class BookSearchQuery:
    def __init__(self, title: str = "", author: str = "", isbn: str = "") -> None:
        self._title = title
        self._author = author
        self._isbn = isbn

    @property
    def title(self) -> str:
        """
        Returns
        -------
        str
            検索する本のタイトル
        """
        return self._title

    @property
    def author(self) -> str:
        return self._author

    @property
    def isbn(self) -> str:
        return self._isbn

    def get_dict(self) -> Dict:
        data: Dict = {}
        if self._title is not "":
            data["title"] = self._title
            print("search by title. value={}".format(self._title))
        if self._author is not "":
            data["author"] = self._author
            print("search by author value={}".format(self._author))
        if self._isbn is not "":
            data["isbn"] = self._isbn
            print("search by isbn value={}".format(self._isbn))
        return data
