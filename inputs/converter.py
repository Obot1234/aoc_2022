from abc import ABC, abstractmethod
from typing import TypeVar, Generic

T = TypeVar('T')


class Converter(ABC, Generic[T]):
    @abstractmethod
    def convert(self, daily_input: [str]) -> T:
        pass


class ListOfNumbersConverter(Converter[list[list[int]]]):
    def convert(self, daily_input: [str]) -> list[list[int]]:
        big_list = []
        small_list = []
        for val in daily_input:
            if len(val) == 0:
                big_list.append(small_list)
                small_list = []
            else:
                small_list.append(int(val))
        return big_list
