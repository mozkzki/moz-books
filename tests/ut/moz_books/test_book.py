from moz_books.book import Book


class TestBook:
    def test_str(self) -> None:
        book = Book()
        print(book)
