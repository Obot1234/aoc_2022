import numpy as np


class Rope:
    def __init__(self, length) -> None:
        self.components = np.zeros((length, 2))
        self.positions = set()

    def move(self, movement: np.ndarray, count: int) -> None:
        for k in range(count):
            self.components[0] += movement
            self.move_tail()
            tail = self.components[-1]
            self.positions.add((tail[0], tail[1]))

    def move_tail(self) -> None:
        for k in range(1, len(self.components)):
            distance = self.components[k - 1] - self.components[k]
            if -1 <= distance[0] <= 1 and -1 <= distance[1] <= 1:
                return
            else:
                self.components[k] += np.sign(distance)
