from day import Day
from inputs.converter import ListConverter
from scoring import day_2_1_scoring, day_2_2_scoring


class RockPaperScissors:
    def __init__(self, input_line: str):
        self.first_item, self.second_item = input_line.split()

    def score(self, fun) -> int:
        return fun(self.first_item, self.second_item)


class Day2(Day):
    def __init__(self) -> None:
        super().__init__(2)
        self.strategies = ListConverter(RockPaperScissors).convert(self.input)

    def part1(self) -> int:
        return sum(strategy.score(day_2_1_scoring) for strategy in self.strategies)

    def part2(self) -> int:
        return sum(strategy.score(day_2_2_scoring) for strategy in self.strategies)


if __name__ == '__main__':
    Day2().lets_go()
