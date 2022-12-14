import time
from abc import ABC, abstractmethod
from typing import TypeVar, Generic

from inputs.daily_input import DailyInput

T = TypeVar('T')


class Day(ABC, Generic[T]):
    def __init__(self, day: int, test=False):
        self.start = time.perf_counter()
        self.day = day
        self.input = DailyInput(day, test).get()

    def lets_go(self) -> None:
        time_parsing = (time.perf_counter() - self.start) * 1000
        time_part1, ans1 = self.__time_part(self.part1)
        time_part2, ans2 = self.__time_part(self.part2)
        self.pretty_print_execution_time(time_parsing, time_part1, time_part2)
        print(ans1)
        print(ans2)

    def pretty_print_execution_time(self, time_parsing, time_part_1, time_part_2) -> None:
        time_total = time_parsing + time_part_1 + time_part_2
        print(f"| {self.day:3} | {time_total:8.2f} ms | {time_parsing:8.2f} ms | "
              f"{time_part_1:8.2f} ms |  {time_part_2:8.2f} ms |")

    @staticmethod
    def __time_part(part) -> (float, T):
        start = time.perf_counter()
        ans = part()
        time_spent = time.perf_counter() - start
        return time_spent * 1000, ans  # in ms

    @abstractmethod
    def part1(self) -> T:
        pass

    @abstractmethod
    def part2(self) -> T:
        pass
