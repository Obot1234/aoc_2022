from day import Day


class Today(Day[int]):
    def __init__(self) -> None:
        super().__init__(0)

    def part1(self) -> int:
        return 0

    def part2(self) -> int:
        return 0


if __name__ == '__main__':
    Today().lets_go()
