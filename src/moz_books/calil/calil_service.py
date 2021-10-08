import json
from time import sleep
from typing import Dict, List

import requests
from moz_books.book import Book
from moz_books.search_params import SearchParams
from moz_books.calil.calil_book_factory import CalilBookFactory
from moz_books.calil.calil_request_params_factory import CalilRequestParamsFactory
from moz_books.log import get_logger
from moz_books.service import Service

LOGGER = get_logger(__name__)


class CalilService(Service):
    CALIL_BASE_URL = "http://api.calil.jp/check"

    def __init__(self):
        super().__init__(
            self.__class__.__name__,
            CalilService.CALIL_BASE_URL,
            CalilBookFactory(),
            CalilRequestParamsFactory(),
        )

    def search_books(self, query: SearchParams) -> List[Book]:
        response_json = self._request(query)
        new_response_json = self._polling(response_json)
        # 検索パラメーターを追加
        new_response_json = self._add_param(new_response_json, query)
        LOGGER.debug(json.dumps(new_response_json, sort_keys=True, indent=4))
        return self._book_factory.create_list(new_response_json)

    def _polling(self, response_json: Dict) -> Dict:
        while response_json["continue"] == 1:
            sleep(2)
            response_json = self._polling_request(response_json["session"])
        # continueが1以外なら終了、そのレスポンスを戻す
        return response_json

    def _polling_request(self, session: str) -> Dict:
        response: requests.models.Response = requests.get(
            CalilService.CALIL_BASE_URL, params={"session": session}
        )
        # status codeが200番台以外なら例外発生
        response.raise_for_status()
        # 2回目以降のレスポンスはJSONP固定になるため
        json_string = response.text[9:-2]
        response_json = json.loads(json_string)

        return response_json

    def _add_param(self, response_json: Dict, query: SearchParams) -> Dict:
        new_response_json = response_json.copy()
        new_response_json["isbn"] = query.isbn
        new_response_json["systemid1"] = "Tokyo_Nerima"
        return new_response_json
