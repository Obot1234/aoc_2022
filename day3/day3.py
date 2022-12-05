from typing import TypeVar

from inputs.converter import ListConverter
from inputs.daily_input import DailyInput

T = TypeVar('T')


def item_to_priority(item: str) -> int:
    val = ord(item)
    return val - 38 if val <= ord("Z") else val - 96


class Rucksack:
    def __init__(self, contents: str):
        content_split = len(contents) // 2
        self.compartments = [contents[:content_split],
                             contents[content_split:]]

    def get_double_item(self) -> str:
        return set(self.compartments[0]).intersection(self.compartments[1]).pop()

    def contents(self) -> str:
        return "".join(self.compartments)


class Group:
    def __init__(self, _rucksacks: list[Rucksack]):
        self.rucksacks = _rucksacks

    def get_common_item(self) -> str:
        res = set(self.rucksacks[0].contents())
        for rucksack in self.rucksacks[1:]:
            res = res.intersection(rucksack.contents())
        return res.pop()


def batched(_list: list[T], n: int) -> list[list[T]]:
    for k in range(0, len(_list), n):
        if k + n <= len(_list):
            yield _list[k:(k + n)]


def part1(_rucksacks: list[Rucksack]) -> int:
    return sum([item_to_priority(rucksack.get_double_item()) for rucksack in rucksacks])


def part2(_groups: list[Group]) -> int:
    return sum([item_to_priority(group.get_common_item()) for group in groups])


if __name__ == '__main__':
    daily_input = DailyInput(3).get()
    rucksacks = ListConverter(Rucksack).convert(daily_input)
    print(f"Part 1: {part1(rucksacks)}")
    groups = [Group(batch) for batch in batched(rucksacks, 3)]
    print(f"Part 2: {part2(groups)}")
