import argparse
from .core import search_by_isbn, search, search_price
from mmbooks.rakuten import Rakuten
from mmbooks.google import Google
from mmbooks.opendb import OpenDB
from mmbooks.calil import Calil


def main():
    parser = argparse.ArgumentParser(
        description="""
    本の情報を検索します。
    """
    )

    # 必須の引数
    # parser.add_argument("arg1", help="この引数の説明（なくてもよい）")
    # parser.add_argument("arg2", help="foooo")

    # オプション引数（指定しなくても良い引数）を追加
    parser.add_argument("-t", "--title", help="検索する本のタイトル")
    parser.add_argument("-a", "--author", help="検索する本の著者名")
    parser.add_argument("-i", "--isbn", help="検索する本のISBN")
    parser.add_argument(
        "-s",
        "--service",
        help="検索に利用するサービス",
        default="rakuten",
        choices=["rakuten", "google", "opendb", "calil"],
    )

    # よく使う引数なら省略形があると使う時に便利
    # parser.add_argument("-a", "--arg4")

    parser.add_argument("-p", "--price", help="価格を網羅的に調査する場合に指定", action="store_true")

    args = parser.parse_args()

    if args.service == "rakuten":
        service = Rakuten()
    elif args.service == "google":
        service = Google()
    elif args.service == "opendb":
        service = OpenDB()
    elif args.service == "calil":
        service = Calil()
    else:
        service = Rakuten()

    if args.isbn is not None and args.isbn is not "":
        if args.price:
            books = search_price(args.isbn)
            print(books)
            return
        book = search_by_isbn(args.isbn, service=service)
        print(book)
    elif args.title is not None or args.author is not None:
        books = search(title=args.title, author=args.author, service=service)
        print(books)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
