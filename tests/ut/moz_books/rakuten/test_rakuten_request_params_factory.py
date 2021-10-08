import os

import pytest
from moz_books.exception import NotFoundEnvValueError
from moz_books.rakuten.rakuten_request_params_factory import RakutenRequestParamsFactory
from moz_books.search_params import SearchParams


class TestRakutenRequestParamsFactory:
    @pytest.fixture()
    def factory(self):
        return RakutenRequestParamsFactory()

    def test_create(self, factory: RakutenRequestParamsFactory):
        params = SearchParams(isbn="1111", title="title1", author="author1")
        _, actual = factory.create(params)
        assert actual["isbn"] == "1111"
        assert actual["title"] == "title1"
        assert actual["author"] == "author1"
        assert actual["applicationId"] == os.environ.get("rakuten_app_id")
        assert actual["sort"] == "sales"

    def test_create_not_rakuten_app_id(self, factory: RakutenRequestParamsFactory):
        params = SearchParams()
        temp = os.environ.pop("rakuten_app_id")
        with pytest.raises(NotFoundEnvValueError, match="Must specify RAKUTEN_APP_ID."):
            factory.create(params)
        os.environ["rakuten_app_id"] = temp
