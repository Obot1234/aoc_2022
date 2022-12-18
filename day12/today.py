from typing import Optional

from day import Day
from day12.map_graph import ReverseMapGraph, MapGraph
from day12.node import MountainCoord
from inputs.converter import Converter


class MountainPassConverter(Converter[tuple[list[list[MountainCoord]], MountainCoord, MountainCoord]]):
    def __init__(self) -> None:
        self.start: Optional[MountainCoord] = None
        self.end: Optional[MountainCoord] = None

    def convert(self, daily_input: [str]) -> (list[list[MountainCoord]], MountainCoord, MountainCoord):
        height_map = []
        prev_map_line = None
        for y, line in enumerate(daily_input):
            map_line = []
            for x, char in enumerate(line):
                node = self.make_node(x, y, char)
                if x > 0:
                    self.link_nodes(map_line[-1], node)
                if y > 0:
                    self.link_nodes(prev_map_line[x], node)
                map_line.append(node)
            height_map.append(map_line)
            prev_map_line = map_line
        return height_map, self.start, self.end

    def make_node(self, x: int, y: int, char: str) -> MountainCoord:
        if char == 'S':
            node = MountainCoord(x, y, 1)
            self.start = node
        elif char == "E":
            node = MountainCoord(x, y, 26)
            self.end = node
        else:
            value = ord(char) - 96
            node = MountainCoord(x, y, value)
        return node

    @staticmethod
    def link_nodes(first_node: MountainCoord, second_node: MountainCoord) -> None:
        first_node.append(second_node)
        second_node.append(first_node)


class Today(Day[int]):
    def __init__(self) -> None:
        super().__init__(12, test=False)
        self.mountain, self.start_pos, self.end_pos = MountainPassConverter().convert(self.input)

    def part1(self) -> int:
        shortest_path = MapGraph(self.mountain).find_shortest_path(self.start_pos, self.end_pos)
        # self.draw_map("../artifacts/day12_shortest_path", shortest_path)
        return len(shortest_path) - 1

    def part2(self) -> int:
        shortest_path = ReverseMapGraph(self.mountain).find_shortest_path(self.end_pos, None)
        # self.draw_map("../artifacts/day12_best_hike", shortest_path)
        return len(shortest_path) - 1

    def draw_map(self, name: str, path: list[MountainCoord]) -> None:
        import matplotlib.pyplot as plt
        import numpy as np
        fig, ax = plt.subplots()
        height_map = np.array([[node.height for node in node_list] for node_list in self.mountain])
        shortest_route = np.array([(node.x, node.y) for node in path])
        ax.imshow(height_map)
        ax.set_axis_off()
        ax.plot(shortest_route[:, 0], shortest_route[:, 1])
        plt.subplots_adjust(wspace=0, hspace=0)
        plt.savefig(name, dpi=1000, bbox_inches="tight", transparent=True)


if __name__ == '__main__':
    Today().lets_go()
