import os

import pytest
from moz_books.calil.calil_request_params_factory import CalilRequestParamsFactory
from moz_books.exception import InvalidSearchParamsError, NotFoundEnvValueError
from moz_books.search_params import SearchParams


class TestCalilRequestParamsFactory:
    @pytest.fixture()
    def factory(self):
        return CalilRequestParamsFactory()

    def test_create_not_isbn(self, factory: CalilRequestParamsFactory):
        params = SearchParams()  # isbn指定なし
        with pytest.raises(InvalidSearchParamsError, match="Must specify isbn."):
            factory.create(params)

    @pytest.mark.parametrize("isbn", [(""), (None)])
    def test_create_empty_isbn(self, isbn, factory: CalilRequestParamsFactory):
        params = SearchParams(isbn=isbn)
        with pytest.raises(InvalidSearchParamsError, match="Must specify isbn."):
            factory.create(params)

    def test_create_not_calil_app_key(self, factory: CalilRequestParamsFactory):
        params = SearchParams(isbn="12345")
        temp = os.environ.pop("calil_app_key")
        with pytest.raises(NotFoundEnvValueError, match="Must specify CALIL_APP_KEY."):
            factory.create(params)
        os.environ["calil_app_key"] = temp

    def test_create(self, factory: CalilRequestParamsFactory):
        params = SearchParams(isbn="12345")
        _, actual = factory.create(params)
        assert actual["isbn"] == "12345"
        assert actual["appkey"] == "dummy"
        assert actual["format"] == "json"
        assert actual["callback"] == "no"
        assert actual["systemid1"] == "Tokyo_Nerima"
        assert actual["systemid2"] == "Special_Jil"
        assert actual["systemid"] == "Tokyo_Nerima,Special_Jil"
