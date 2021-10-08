from typing import Dict, Tuple
from moz_books.interface.i_request_params_factory import IRequestParamsFactory
from moz_books.search_params import SearchParams
from moz_books.service import LOGGER


class GoogleRequestParamsFactory(IRequestParamsFactory):
    def create(self, search_params: SearchParams) -> Tuple[str, Dict]:
        query_param: Dict = search_params.get_dict()
        isbn = query_param.get("isbn", "")
        title = query_param.get("title", "")
        author = query_param.get("author", "")

        query_dic = {}
        if isbn:
            query_dic["isbn"] = isbn
        else:
            if title:
                query_dic["intitle"] = title
            if author:
                query_dic["inauthor"] = author

        # q=isbn:9784532280208
        # q=intitle:カンブリア+inauthor:村上
        query_string = "+".join("%s:%s" % (k, v) for k, v in query_dic.items())

        params: Dict = {
            "q": query_string,
            "maxResults": str(40),
            "printType": "books",
            # "langRestrict": "ja",  # 機能しなくなったようだ
        }
        # 文字列にしないと「:」等がURLエンコードされてしまう
        params_str = "&".join("%s=%s" % (k, v) for k, v in params.items())
        LOGGER.debug(params_str)
        return (params_str, params)
