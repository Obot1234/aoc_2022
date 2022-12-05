import copy

from crates import Crates
from day import Day
from inputs.converter import ListConverter, InputSplitter
from move import Move


class Today(Day[str]):
    def __init__(self) -> None:
        super().__init__(5)
        self.inputs = InputSplitter().convert(self.input)
        self.crates = Crates(self.inputs[0])
        self.moves = ListConverter(Move).convert(self.inputs[1])

    def part1(self) -> str:
        crate_copy = copy.deepcopy(self.crates)
        for move in self.moves:
            crate_copy.apply_move_9000(move)
        return crate_copy.get_top_stack_message()

    def part2(self) -> str:
        crate_copy = copy.deepcopy(self.crates)
        for move in self.moves:
            crate_copy.apply_move_9001(move)
        return crate_copy.get_top_stack_message()


if __name__ == '__main__':
    Today().lets_go()
