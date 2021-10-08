import os
from typing import Dict, Tuple
from moz_books.exception.invalid_search_params_error import InvalidSearchParamsError
from moz_books.exception.not_found_env_value_error import NotFoundEnvValueError

from moz_books.interface.i_request_params_factory import IRequestParamsFactory
from moz_books.search_params import SearchParams
from moz_books.log import get_logger

LOGGER = get_logger(__name__)


class CalilRequestParamsFactory(IRequestParamsFactory):
    def create(self, search_params: SearchParams) -> Tuple[str, Dict]:
        if not search_params.isbn:
            raise InvalidSearchParamsError("Must specify isbn.")
        if not os.environ.get("calil_app_key"):
            raise NotFoundEnvValueError("Must specify CALIL_APP_KEY.")

        params: Dict = {}
        params["isbn"] = search_params.isbn
        params["appkey"] = os.environ.get("calil_app_key")
        params["format"] = "json"
        params["callback"] = "no"
        params["systemid1"] = "Tokyo_Nerima"
        params["systemid2"] = "Special_Jil"
        params["systemid"] = params["systemid1"] + "," + params["systemid2"]

        params_str = "&".join("%s=%s" % (k, v) for k, v in params.items())
        LOGGER.debug(params_str)
        return (params_str, params)
