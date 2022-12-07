from dataclasses import dataclass


@dataclass
class File:
    name: str
    size: int

    def print(self, starting_spaces: str = ""):
        print(f"{starting_spaces} {self.name}:{self.size}")
