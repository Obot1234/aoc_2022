from day import Day
from day11.monkey import Monkey


class Today(Day[int]):
    def __init__(self) -> None:
        super().__init__(11)
        self.do_test = False

    @staticmethod
    def do_round(monkeys) -> None:
        for monkey in monkeys:
            monkey.inspect()

    def part1(self) -> int:
        monkeys = self.get_monkeys(managed_worries=True)
        for k in range(20):
            self.do_round(monkeys)
        monkey_business = sorted([monkey.items_inspected for monkey in monkeys])[-2:]
        return monkey_business[0] * monkey_business[1]

    def part2(self) -> int:
        monkeys = self.get_monkeys(managed_worries=False)
        for k in range(10000):
            self.do_round(monkeys)
        monkey_business = sorted([monkey.items_inspected for monkey in monkeys])[-2:]
        return monkey_business[0] * monkey_business[1]

    def get_monkeys(self, managed_worries: bool) -> list[Monkey]:
        return self.get_test_monkeys(managed_worries) if self.do_test \
            else self.get_normal_monkeys(managed_worries)

    @staticmethod
    def get_test_monkeys(managed_worries: bool) -> list[Monkey]:
        monkeys = [Monkey([79, 98], lambda x: x * 19, 23),
                   Monkey([54, 65, 75, 74], lambda x: x + 6, 19),
                   Monkey([79, 60, 97], lambda x: x * x, 13),
                   Monkey([74], lambda x: x + 3, 17)]
        for monkey, (true_id, false_id) in zip(monkeys, [(2, 3), (2, 0), (1, 3), (0, 1)]):
            monkey.set_monkeys(monkeys[true_id], monkeys[false_id])
            monkey.managed_worries = managed_worries
        return monkeys

    @staticmethod
    def get_normal_monkeys(managed_worries: bool) -> list[Monkey]:
        monkeys = [Monkey([89, 74], lambda x: x * 5, 17),
                   Monkey([75, 69, 87, 57, 84, 90, 66, 50], lambda x: x + 3, 7),
                   Monkey([55], lambda x: x + 7, 13),
                   Monkey([69, 82, 69, 56, 68], lambda x: x + 5, 2),
                   Monkey([72, 97, 50], lambda x: x + 2, 19),
                   Monkey([90, 84, 56, 92, 91, 91], lambda x: x * 19, 3),
                   Monkey([63, 93, 55, 53], lambda x: x * x, 5),
                   Monkey([50, 61, 52, 58, 86, 68, 97], lambda x: x + 4, 11),
                   ]
        ids = [(4, 7), (3, 2), (0, 7), (0, 2), (6, 5), (6, 1), (3, 1), (5, 4)]
        for monkey, (true_id, false_id) in zip(monkeys, ids):
            monkey.set_monkeys(monkeys[true_id], monkeys[false_id])
            monkey.managed_worries = managed_worries
        return monkeys


if __name__ == '__main__':
    Today().lets_go()
