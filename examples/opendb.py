from moz_books import OpenDB, SearchParams
from moz_books.log import get_logger

LOGGER = get_logger(__name__)


def search(params: SearchParams):
    books = OpenDB().search_books(params)
    for book in books:
        LOGGER.info(book)


def main() -> None:
    # isbn検索以外非対応
    # search(SearchParams(title="5秒後に意外な"))
    # search(SearchParams(author="桃戸ハル"))
    search(SearchParams(isbn="9784052046209"))  # 5秒後に意外な結末ミノタウロスの青い迷宮
    search(SearchParams(isbn="9784532280208"))  # カンブリア宮殿村上龍の質問術


if __name__ == "__main__":
    main()
