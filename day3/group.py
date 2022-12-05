from rucksack import Rucksack


class Group:
    def __init__(self, _rucksacks: list[Rucksack]):
        self.rucksacks = _rucksacks

    def get_common_item(self) -> str:
        res = set(self.rucksacks[0].contents())
        for rucksack in self.rucksacks[1:]:
            res = res.intersection(rucksack.contents())
        return res.pop()
