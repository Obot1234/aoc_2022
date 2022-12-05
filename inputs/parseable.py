from abc import ABC
from typing import TypeVar, Generic

T = TypeVar('T')


class Parseable(ABC, Generic[T]):

    @staticmethod
    def parse(input_string: str) -> T:
        pass
