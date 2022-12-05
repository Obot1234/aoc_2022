from scoring import day_2_1_scoring, day_2_2_scoring
from inputs.converter import ListConverter
from inputs.daily_input import DailyInput


class RockPaperScissors:
    def __init__(self, input_line: str):
        self.first_item, self.second_item = input_line.split()

    def score(self, fun) -> int:
        return fun(self.first_item, self.second_item)


def part1(strategies: list[RockPaperScissors]) -> int:
    return sum(strategy.score(day_2_1_scoring) for strategy in strategies)


def part2(strategies: list[RockPaperScissors]) -> int:
    return sum(strategy.score(day_2_2_scoring) for strategy in strategies)


if __name__ == '__main__':
    daily_input = DailyInput(2).get()
    strategies = ListConverter(RockPaperScissors).convert(daily_input)
    print(f"Part 1: {part1(strategies)}")
    print(f"Part 2: {part2(strategies)}")
