from day import Day
from inputs.converter import ListOfNumbersConverter


class Day1(Day):
    def __init__(self) -> None:
        super().__init__(1)
        self.bags = ListOfNumbersConverter().convert(self.input)

    def part1(self) -> int:
        calories_per_bag = [sum(content) for content in self.bags]
        return max(calories_per_bag)

    def part2(self) -> int:
        calories_per_bag = [sum(content) for content in self.bags]
        return sum(sorted(calories_per_bag)[-3:])


if __name__ == '__main__':
    Day1().lets_go()
