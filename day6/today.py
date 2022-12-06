from day import Day


class Today(Day[int]):
    def __init__(self) -> None:
        super().__init__(6)

    @staticmethod
    def find_unique_pattern(full_input: str, min_length: int) -> int:
        for k, length in enumerate(len(set(full_input[k:k + min_length])) for k in range(len(full_input))):
            if length == min_length:
                return k + min_length
        return k

    def part1(self) -> int:
        return self.find_unique_pattern(self.input[0], 4)

    def part2(self) -> int:
        return self.find_unique_pattern(self.input[0], 14)


if __name__ == '__main__':
    Today().lets_go()
