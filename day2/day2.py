from day import Day
from rock_paper_scissors import RockPaperScissors
from inputs.converter import ListConverter
from scoring import day_2_1_scoring, day_2_2_scoring


class Today(Day):
    def __init__(self) -> None:
        super().__init__(2)
        self.strategies = ListConverter(RockPaperScissors).convert(self.input)

    def part1(self) -> int:
        return sum(strategy.score(day_2_1_scoring) for strategy in self.strategies)

    def part2(self) -> int:
        return sum(strategy.score(day_2_2_scoring) for strategy in self.strategies)


if __name__ == '__main__':
    Today().lets_go()
