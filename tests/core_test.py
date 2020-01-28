import mmbooks.core as mmbook
from mmbooks.rakuten import Rakuten


class TestCore:
    def setup(self):
        pass

    def test_search_by_title(self):
        books = mmbook.search(title="5秒後に意外な", service=Rakuten())
        print(books)

    # def test_search_by_author(self):
    #     books = mmbook.search_by_author(author="")
    #     print(books)

    def test_search_by_isbn(self):
        book = mmbook.search_by_isbn("9784532280208", service=Rakuten())
        print(book)
