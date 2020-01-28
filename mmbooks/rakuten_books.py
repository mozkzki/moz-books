from typing import Dict, List
from mmbooks.book import Book
from mmbooks.books import Books
from mmbooks.rakuten_book import RakutenBook


class RakutenBooks(Books):
    def __init__(self, response_json: Dict):
        super().__init__(response_json)

    def _get_book_list(self, response_json: Dict) -> List[Book]:
        books: List = []
        total_count = 0
        for item in response_json.get("Items", ""):
            books.append(RakutenBook(item.get("Item")))
            total_count += 1
        print("found {} items.".format(total_count))
        return books

    # def get_message(self):
    #     if self.length() == 0:
    #         return "見つかりませんでした。。"

    #     columns = []
    #     for rakuten_book in self.rakuten_books:

    #         image = Image()
    #         path = image.download(rakuten_book.image_url)
    #         image_magic = ImageMagic()
    #         image_magic.convert(path)
    #         gyazo = Gyazo()
    #         gyazo_url = gyazo.upload(path)

    #         text = (
    #             "著:"
    #             + rakuten_book.author
    #             + "\n￥"
    #             + str(rakuten_book.price)
    #             + "\n発売日:"
    #             + rakuten_book.sales_date
    #         )
    #         text = text[:60]
    #         column = CarouselColumn(
    #             thumbnail_image_url=gyazo_url,
    #             title=rakuten_book.title[:40],
    #             text=text,
    #             actions=[
    #                 PostbackTemplateAction(label="借りる / 買う", data="isbn:" + rakuten_book.isbn)
    #             ],
    #         )
    #         columns.append(column)

    #     return CarouselTemplate(columns=columns)
