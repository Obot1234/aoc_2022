from typing import Optional


class MountainCoord(list['MountainCoord']):
    def __init__(self, x: int, y: int, value: int) -> None:
        super().__init__()
        self.x = x
        self.y = y
        self.height = value
        self.road_to_start = None
        self.distance_from_start = 99999999999999999999  # something BIG

    def distance_to(self, other: Optional['MountainCoord']) -> int:
        if other is None:
            return 0
        return abs(self.x - other.x) + abs(self.y - other.y)

    def __eq__(self, other: 'MountainCoord') -> bool:
        return self.x == other.x and self.y == other.y

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def __cmp__(self, other: 'MountainCoord') -> int:
        return self.distance_from_start - other.distance_from_start

    def __str__(self) -> str:
        return f"({self.x},{self.y})"

    def __repr__(self) -> str:
        return f"({self.x},{self.y})"
