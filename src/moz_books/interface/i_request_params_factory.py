from abc import ABC, abstractmethod
from typing import Dict, Tuple

from moz_books.search_params import SearchParams


class IRequestParamsFactory(ABC):
    @abstractmethod
    def create(self, query: SearchParams) -> Tuple[str, Dict]:
        """abstract"""
