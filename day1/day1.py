from inputs.converter import ListOfNumbersConverter
from inputs.daily_input import DailyInput


def part1(bags: list[list[int]]):
    calories_per_bag = [sum(content) for content in bags]
    return max(calories_per_bag)


def part2(bags: list[list[int]]):
    calories_per_bag = [sum(content) for content in bags]
    return sum(sorted(calories_per_bag)[-3:])


if __name__ == '__main__':
    daily_input = DailyInput(1).get()
    bags = ListOfNumbersConverter().convert(daily_input)
    print(f"Part 1: {part1(bags)}")
    print(f"Part 2: {part2(bags)}")
