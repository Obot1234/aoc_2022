from inputs.converter import Converter


class Program(Converter['Program']):

    def __init__(self) -> None:
        self.ops = [1]

    def convert(self, daily_input: [str]) -> 'Program':
        for op in daily_input:
            self.add_op(op)
        return self

    def add_op(self, op: str):
        if op[0] == 'n':
            self.ops.append(self.ops[-1])
        else:
            self.ops.append(self.ops[-1])
            self.ops.append(self.ops[-1] + int(op[5:]))

    def get_strength_at(self, values: list[int]):
        total = 0
        for value in values:
            strength = self.ops[value - 1]
            total += strength * value
        return total

    def draw(self, width: int) -> str:
        ans = ""
        for k, value in enumerate(self.ops):
            if k % width == 0 and k != 0:
                ans += "\n"
            if -1 <= (k % width) - value <= 1:
                ans += "#"
            else:
                ans += "."
        return ans
