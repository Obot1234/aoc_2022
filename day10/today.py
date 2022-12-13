from day import Day
from day10.program import Program


class Today(Day[int]):
    def __init__(self) -> None:
        super().__init__(10)
        self.program = Program().convert(self.input)

    def part1(self) -> int:
        return self.program.get_strength_at([20, 60, 100, 140, 180, 220])

    def part2(self) -> str:
        ans = self.program.draw(40)
        return ans


if __name__ == '__main__':
    Today().lets_go()
