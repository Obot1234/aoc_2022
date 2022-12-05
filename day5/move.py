from abc import ABC
from dataclasses import dataclass

from inputs.parseable import Parseable


@dataclass
class Move(Parseable['Move']):
    count: int
    move_from: int
    move_to: int

    @staticmethod
    def parse(input_string: str) -> 'Move':
        inputs = [int(s) for s in input_string.split() if s.isdigit()]
        return Move(inputs[0], inputs[1] - 1, inputs[2] - 1)
