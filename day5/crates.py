from move import Move


class Crates:
    def __init__(self, initial_setup: list[str]):
        self.stacks_count = int(initial_setup[-1].split()[-1])
        self.stacks = [[] for _ in range(self.stacks_count)]
        for line in initial_setup[-2::-1]:
            for pos in range(0, self.stacks_count):
                crate_location_in_input = pos * 4 + 1
                crate_content = line[crate_location_in_input]
                if crate_content != ' ':
                    self.stacks[pos].append(crate_content)

    def apply_move_9000(self, move: Move) -> None:
        stack = self.grab_crates(move.move_from, move.count)
        stack.reverse()
        self.stacks[move.move_to].extend(stack)

    def apply_move_9001(self, move: Move) -> None:
        stack = self.grab_crates(move.move_from, move.count)
        self.stacks[move.move_to].extend(stack)

    def grab_crates(self, move_from: int, count: int):
        stack = self.stacks[move_from][-count:]
        self.stacks[move_from] = self.stacks[move_from][:-count]
        return stack

    def get_top_stack_message(self) -> str:
        return "".join([stack[-1] for stack in self.stacks])
