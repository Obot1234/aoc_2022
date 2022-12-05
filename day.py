import time
from abc import ABC, abstractmethod

from inputs.daily_input import DailyInput


class Day(ABC):
    def __init__(self, day: int):
        self.input = DailyInput(day).get()

    def lets_go(self) -> None:
        time_part1 = self.__time_part(self.part1)
        time_part2 = self.__time_part(self.part2)

        print(f"Total time: {time_part1 + time_part2}ms")

    @staticmethod
    def __time_part(part) -> float:
        start = time.perf_counter()
        ans = part()
        time_spent = time.perf_counter() - start
        print(ans)
        return time_spent * 1000  # in ms

    @abstractmethod
    def part1(self) -> int:
        pass

    @abstractmethod
    def part2(self) -> int:
        pass
