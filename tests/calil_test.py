import pytest
import json
from unittest.mock import patch, MagicMock
from mmbooks.calil import Calil
from mmbooks.book_search_query import BookSearchQuery


class TestCalil:
    @pytest.mark.slow
    def test_get_book(self):
        query = BookSearchQuery(isbn="9784532280208")
        calil_book = Calil().get_book(query)
        print(calil_book)

    @pytest.mark.slow
    def test_get_book_error(self):
        # isbnを指定しないクエリはエラーになる
        query = BookSearchQuery()
        with pytest.raises(Exception):
            Calil().get_book(query)

    def test_get_one_book_from_json(self):
        response_json = json.loads(
            '{"isbn":"1111","systemid1":"system1","books":{"1111":{"system1":{"test":"hoge","status":"OK"}}}}'
        )
        books = Calil()._get_books(response_json)
        assert books.list[0].isbn == "1111"

    # @pytest.mark.slow
    # def test_polling(self):
    #     with patch("kbot.book.calil.calil._CalilService__polling_request") as mock:
    #         json_data = json.loads('{"continue": 1, "session": "hoge"}')
    #         calil._CalilService__polling(json_data)
    #         mock.assert_called_once()

    # def test_polling_request(self):
    #     with patch("kbot.book.calil.CalilService._CalilService__request_sub") as mock:
    #         response_mock = MagicMock()
    #         response_mock.text = 'callback({"books": {"1111":{"system1":{"test":"hoge"}}}} )'
    #         mock.return_value = response_mock
    #         query = BookSearchQuery()
    #         result = calil._CalilService__polling_request(query)
    #         mock.assert_called_once()
    #         assert json.dumps(result) == '{"books": {"1111": {"system1": {"test": "hoge"}}}}'


# class TestCalilQuery(object):
#     def test_adjust_next_query(self):
#         query = BookSearchQuery()
#         query.set("foo", "bar")
#         result = CalilQuery.adjust_next_query(query)
#         assert result.get("foo") == query.get("foo")
