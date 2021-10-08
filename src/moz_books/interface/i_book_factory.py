from abc import ABC, abstractmethod
from typing import Dict, List, Union
from moz_books.book import Book


class IBookFactory(ABC):
    @abstractmethod
    def create(cls, response_json: Dict) -> Book:
        """abstract"""

    @abstractmethod
    def create_list(cls, response_json: Union[Dict, List]) -> List[Book]:
        """abstract"""
