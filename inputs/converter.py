from abc import ABC, abstractmethod
from collections.abc import Callable
from typing import TypeVar, Generic, Union

from inputs.parseable import Parseable

T = TypeVar('T')
V = TypeVar('V')


class Converter(ABC, Generic[T]):
    @abstractmethod
    def convert(self, daily_input: [str]) -> T:
        pass


class ListConverter(Generic[V], Converter[list[V]]):
    def __init__(self, constructor: Union[Callable[[str], V], Parseable[V]]):
        self.constructor = constructor

    def convert(self, daily_input: [str]) -> list[V]:
        return [self.convert_line(input_line) for input_line in daily_input]

    def convert_line(self, line_input: str) -> V:
        if issubclass(self.constructor, Parseable):
            return self.constructor.parse(line_input)
        else:
            return self.constructor(line_input)


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
        big_list.append(small_list)
        return big_list


class InputSplitter(Converter[list[list[str]]]):
    def convert(self, daily_input: [str]) -> list[list[str]]:
        big_list = []
        small_list = []
        for val in daily_input:
            if len(val) == 0:
                big_list.append(small_list)
                small_list = []
            else:
                small_list.append(val)
        big_list.append(small_list)
        return big_list
