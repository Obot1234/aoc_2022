from inputs.converter import ListOfNumbersConverter
from inputs.daily_input import DailyInput


def day1_1(bags):
    calories_per_bag = [sum(content) for content in bags]
    return max(calories_per_bag)


def day1_2(bags):
    calories_per_bag = [sum(content) for content in bags]
    return sum(sorted(calories_per_bag)[-3:])


if __name__ == '__main__':
    bags = DailyInput(1).convert(ListOfNumbersConverter())
    print(f"Part 1: {day1_1(bags)}")
    print(f"Part 2: {day1_2(bags)}")
