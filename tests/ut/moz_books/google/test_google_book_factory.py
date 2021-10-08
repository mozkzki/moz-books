import pytest
from moz_books.exception import InvalidResponseError
from moz_books.google.google_book import GoogleBook
from moz_books.google.google_book_factory import GoogleBookFactory
from tests.ut.moz_books.mock_response import google_one_books_response


class TestGoogleBookFactory:
    @pytest.fixture()
    def factory(self):
        return GoogleBookFactory()

    def test_create(self, factory: GoogleBookFactory) -> None:
        item_dic = google_one_books_response().get("items", "")[0]
        book: GoogleBook = factory.create(item_dic)
        assert book.author == "author1"
        assert book.isbn == "9784532280208"
        assert book.isbn10 == "4532280206"
        assert book.title == "title1"
        assert book.description == "description1"
        assert book.page_count == 284
        assert book.image_url == "http://books.google.com/books/content?id=xxxxx"
        assert book.info_url == "http://books.google.co.jp/books?id=yyyyyy"
        assert book.published_date == "2013-10"
        assert book.type == "GoogleBook"

    def test_create_list(self, factory: GoogleBookFactory) -> None:
        books = factory.create_list(google_one_books_response())
        assert books[0].title == "title1"

    @pytest.mark.parametrize(
        "response",
        [
            ({"totalItems": 0, "items": []}),
            ({"totalItems": 0}),
        ],
    )
    def test_create_list_empty(self, response, factory: GoogleBookFactory) -> None:
        books = factory.create_list(response)
        assert len(books) == 0

    @pytest.mark.parametrize(
        "response",
        [
            ({}),
        ],
    )
    def test_create_list_invalid_response(self, response, factory: GoogleBookFactory) -> None:
        with pytest.raises(ValueError):
            factory.create_list(response)

    def test_create_authorが取れない場合(self, factory: GoogleBookFactory) -> None:
        item_dic = google_one_books_response().get("items", "")[0]
        item_dic.get("volumeInfo").pop("authors")
        book: GoogleBook = factory.create(item_dic)
        assert book.author == "UNKNOWN"

    def test_create_isbn13とisbn10がともに取れない場合(self, factory: GoogleBookFactory) -> None:
        item_dic = google_one_books_response().get("items", "")[0]
        item_dic.get("volumeInfo").pop("industryIdentifiers")
        with pytest.raises(InvalidResponseError):
            factory.create(item_dic)
