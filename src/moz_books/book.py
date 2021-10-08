import pprint
from dataclasses import dataclass


@dataclass(frozen=True)
class Book:
    def __str__(self) -> str:
        return "\n" + pprint.pformat(vars(self), width=5, indent=2)
