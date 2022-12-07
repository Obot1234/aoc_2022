from typing import Optional, Iterator


class Directory:
    def __init__(self, parent: Optional['Directory'], name: str):
        self.parent = parent
        self.name = name
        self.dirs: dict[str, Directory] = {}
        self.files: list[int] = []
        self._size = -1

    def append_dir(self, directory: 'Directory') -> None:
        self.dirs[directory.name] = directory

    def append_file(self, file: int) -> None:
        self.files.append(file)

    def get_dir(self, dir_name: str) -> 'Directory':
        return self.dirs[dir_name]

    def print(self, trailing_spaces=0) -> None:
        starting_spaces = " " * trailing_spaces
        if self.size < 100000:
            print(f"{starting_spaces}{self.name} [{self.size}]")
        else:
            print(f"{starting_spaces}{self.name}")

        for directory in self.dirs.values():
            directory.print(trailing_spaces + 1)
        # for file in self.files.values():
        #    file.print(starting_spaces)

    @property
    def size(self) -> int:
        if self._size == -1:
            self._size = sum([directory.size for directory in self.dirs.values()]) + sum(self.files)
        return self._size

    def __iter__(self) -> Iterator:
        for directory in self.dirs.values():
            for subdir in directory:
                yield subdir
        yield self
