from day import Day
from directory import Directory
from inputs.converter import Converter


class CmdConverter(Converter[Directory]):
    def convert(self, daily_input: [str]) -> Directory:
        top_dir = Directory(parent=None, name="/")
        cur_dir = top_dir
        total_dirs = 0
        line: str
        for line in daily_input[1:]:
            if line[2] == "c":  # line.startswith("$ cd"):
                if line[5] == ".":
                    cur_dir = cur_dir.parent
                else:
                    cur_dir = cur_dir.get_dir(line[5:])
            elif line[2] == "l":  # line.startswith("$ ls"):
                continue
            elif line[2] == "r":  # line.startswith("dir"):
                total_dirs += 1
                cur_dir.append_dir(Directory(cur_dir, line[4:]))
            else:
                size, name = line.split(" ")
                cur_dir.append_file(int(size))
        return top_dir


class Today(Day[int]):
    def __init__(self) -> None:
        super().__init__(7)
        self.directory = CmdConverter().convert(self.input)

    def part1(self) -> int:
        return sum([directory.size for directory in self.directory if directory.size <= 100000])

    def part2(self) -> int:
        total_space = 70000000
        space_left = total_space - self.directory.size
        space_required = 30000000 - space_left
        smallest_file_size = self.directory.size

        for directory in self.directory:
            if space_required < directory.size < smallest_file_size:
                smallest_file_size = directory.size
        return smallest_file_size


if __name__ == '__main__':
    Today().lets_go()
