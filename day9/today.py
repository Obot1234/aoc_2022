import numpy as np

from day import Day
from day9.rope import Rope
from inputs.converter import Converter


class RopeConverter(Converter[Rope]):
    def __init__(self, length) -> None:
        self.rope = Rope(length)

    def convert(self, daily_input: [str]) -> int:
        keys = {"U": np.array([0, 1]),
                "D": np.array([0, -1]),
                "L": np.array([-1, 0]),
                "R": np.array([1, 0])}

        for line in daily_input:
            self.rope.move(keys[line[0]], int(line[2:]))

        return len(self.rope.positions)


class Today(Day[int]):
    def __init__(self) -> None:
        super().__init__(9)

    def part1(self) -> int:
        return RopeConverter(2).convert(self.input)

    def part2(self) -> int:
        return RopeConverter(10).convert(self.input)


if __name__ == '__main__':
    Today().lets_go()
