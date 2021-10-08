from abc import ABC, abstractmethod
from typing import List
from moz_books.book import Book
from moz_books.search_params import SearchParams


class IService(ABC):
    @abstractmethod
    def search_books(self, params: SearchParams) -> List[Book]:
        """abstract"""
