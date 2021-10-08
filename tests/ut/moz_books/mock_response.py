import json
from typing import Dict, List


def google_empty_books_response() -> Dict:
    return {"totalItems": 1, "items": []}


def google_one_books_response() -> Dict:
    dic = {
        "totalItems": 1,
        "items": [
            {
                "volumeInfo": {
                    "authors": ["author1", "author2"],
                    "industryIdentifiers": [
                        {"identifier": "4532280206", "type": "ISBN_10"},
                        {"identifier": "9784532280208", "type": "ISBN_13"},
                    ],
                    "title": "title1",
                    "description": "description1",
                    "pageCount": 284,
                    "imageLinks": {
                        "thumbnail": "http://books.google.com/books/content?id=xxxxx",
                    },
                    "infoLink": "http://books.google.co.jp/books?id=yyyyyy",
                    "publishedDate": "2013-10",
                }
            }
        ],
    }
    return dic


def rakuten_book_response(title: str) -> Dict:
    return {
        "title": title,
        "author": "author1",
        "isbn": "1111",
        "itemCaption": "caption1",
        "itemPrice": "500",
        "largeImageUrl": "https://hoge.com/test/big/image.png",
        "itemUrl": "https://hoge.com/test/image.png",
        "publisherName": "publisher1",
        "salesDate": "2020/01/01",
    }


def rakuten_zero_books_response() -> Dict:
    return {"Items": []}


def rakuten_one_books_response() -> Dict:
    return {
        "Items": [
            {
                "Item": rakuten_book_response("title1"),
            },
        ]
    }


def rakuten_two_books_response() -> Dict:
    return {
        "Items": [
            {
                "Item": rakuten_book_response("title1"),
            },
            {
                "Item": rakuten_book_response("title2"),
            },
        ]
    }


def opendb_zero_books_response() -> List:
    return []


def opendb_one_books_response() -> List:
    return [
        {
            "summary": {
                "title": "title1",
                "author": "author1",
                "isbn": "1111",
                "publisher": "publisher1",
                "cover": "https://cover.openbd.jp/xxxxxx.jpg",
                "pubdate": "2013-10",
            }
        }
    ]


def calil_book_response() -> Dict:
    return {
        "isbn": "1111",
        "reserveurl": "https://test.url?BID=2222",
        "libkey": {"Place1": "貸出可"},
    }


def calil_zero_books_response() -> Dict:
    return {
        "continue": 0,
        "isbn": "1111",
        "systemid1": "Tokyo_Nerima",
        "books": {"1111": {"Tokyo_Nerima": {}}},
    }


def calil_one_books_response(status: str) -> Dict:
    return {
        "continue": 0,
        "isbn": "1111",
        "systemid1": "Tokyo_Nerima",
        "books": {
            "1111": {
                "Tokyo_Nerima": {
                    "reserveurl": "https://test.url?BID=2222",
                    "libkey": {"Place1": "貸出可"},
                    "status": status,
                }
            }
        },
    }


def calil_one_books_response_with_continue1(status: str) -> Dict:
    return {
        "continue": 1,
        "session": "sessionid-1",
    }


def calil_one_books_response_with_continue2(status: str) -> str:
    dic = calil_one_books_response(status)
    return json.dumps(dic)
