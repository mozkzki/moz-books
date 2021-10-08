from typing import Dict, Tuple
from moz_books.exception.invalid_search_params_error import InvalidSearchParamsError
from moz_books.log import get_logger
from moz_books.interface.i_request_params_factory import IRequestParamsFactory
from moz_books.search_params import SearchParams

LOGGER = get_logger(__name__)


class OpenDBRequestParamsFactory(IRequestParamsFactory):
    def create(self, search_params: SearchParams) -> Tuple[str, Dict]:
        if not search_params.isbn:
            LOGGER.error("search params: {}".format(search_params.get_dict()))
            raise InvalidSearchParamsError("Must specify isbn.")

        params: Dict = search_params.get_dict()
        params_str = "&".join("%s=%s" % (k, v) for k, v in params.items())
        LOGGER.debug(params_str)
        return (params_str, params)
