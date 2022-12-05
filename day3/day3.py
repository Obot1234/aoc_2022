from day import Day
from inputs.converter import ListConverter
from util.lists import batched


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
