import os
from typing import Dict, Tuple
from moz_books.interface.i_request_params_factory import IRequestParamsFactory
from moz_books.search_params import SearchParams
from moz_books.exception import NotFoundEnvValueError
from moz_books.log import get_logger

LOGGER = get_logger(__name__)


class RakutenRequestParamsFactory(IRequestParamsFactory):
    def create(self, search_params: SearchParams) -> Tuple[str, Dict]:
        if not os.environ.get("rakuten_app_id"):
            raise NotFoundEnvValueError("Must specify RAKUTEN_APP_ID.")

        params: Dict = search_params.get_dict()
        params["applicationId"] = os.environ.get("rakuten_app_id")
        params["sort"] = "sales"

        params_str = "&".join("%s=%s" % (k, v) for k, v in params.items())
        LOGGER.debug(params_str)
        return (params_str, params)
