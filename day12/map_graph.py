from heapq import heappush, heappop
from typing import Optional

from day12.node import MountainCoord


class MapGraph:
    def __init__(self, node_map: list[list[MountainCoord]]) -> None:
        self.node_map = node_map

    def reset_map(self) -> None:
        for node_row in self.node_map:
            for node in node_row:
                node.road_to_start = None
                node.distance_from_start = 999999999999999

    def find_shortest_path(self, start: MountainCoord, end: Optional[MountainCoord]) -> list[MountainCoord]:
        self.reset_map()
        visited_nodes: set[MountainCoord] = set()
        nodes_to_visit: list[(int, MountainCoord)] = []
        k = 0
        start.distance_from_start = 0
        current_node = start
        heappush(nodes_to_visit, (0, k, start))
        while len(nodes_to_visit) > 0:
            _, _, current_node = heappop(nodes_to_visit)

            if self.should_end(current_node, end):
                break
            visited_nodes.add(current_node)
            node: MountainCoord
            next_distance = current_node.distance_from_start + 1
            for node in current_node:
                if node.distance_from_start > next_distance and \
                        self.can_make_step(current_node, node) and \
                        node not in visited_nodes:
                    node.road_to_start = current_node
                    node.distance_from_start = next_distance
                    distance_to_end = node.distance_to(end)
                    k += 1
                    before = len(nodes_to_visit)
                    heappush(nodes_to_visit, (node.distance_from_start + distance_to_end, k, node))
                    assert len(nodes_to_visit) == before + 1
        road_home = [current_node]
        while current_node.road_to_start is not None:
            current_node = current_node.road_to_start
            road_home.append(current_node)
        road_home.reverse()
        return road_home

    @staticmethod
    def can_make_step(first_node: MountainCoord, second_node: MountainCoord) -> bool:
        return first_node.height + 1 >= second_node.height

    def should_end(self, current_node: MountainCoord, end: MountainCoord) -> bool:
        return current_node == end


class ReverseMapGraph(MapGraph):
    @staticmethod
    def can_make_step(first_node: MountainCoord, second_node: MountainCoord) -> bool:
        return second_node.height + 1 >= first_node.height

    def should_end(self, current_node: MountainCoord, end: MountainCoord) -> bool:
        return current_node.height == 1
