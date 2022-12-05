from day import Day
from .rucksack import Rucksack
from group import Group
from inputs.converter import ListConverter
from util.lists import batched


def item_to_priority(item: str) -> int:
    val = ord(item)
    return val - 38 if val <= ord("Z") else val - 96


class Day3(Day):
    def __init__(self) -> None:
        super().__init__(3)
        self.rucksacks = ListConverter(Rucksack).convert(self.input)

    def part1(self) -> int:
        return sum([item_to_priority(rucksack.get_double_item()) for rucksack in self.rucksacks])

    def part2(self) -> int:
        groups = [Group(batch) for batch in batched(self.rucksacks, 3)]
        return sum([item_to_priority(group.get_common_item()) for group in groups])


if __name__ == '__main__':
    Day3().lets_go()
