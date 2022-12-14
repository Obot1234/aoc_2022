import unittest
from typing import Any

from day import Day


class RegressionTestDays(unittest.TestCase):

    def generic_test(self, day: Day, first_answer: Any, second_answer: Any):
        self.assertEqual(day.part1(), first_answer, f"Problem with part 1 of day {day.day}")
        self.assertEqual(day.part2(), second_answer, f"Problem with part 2 of day {day.day}")

    def test_day1(self) -> None:
        from day1.today import Today
        self.generic_test(Today(), 73211, 213958)

    def test_day2(self) -> None:
        from day2.today import Today
        self.generic_test(Today(), 10404, 10334)

    def test_day3(self) -> None:
        from day3.today import Today
        self.generic_test(Today(), 8088, 2522)

    def test_day4(self) -> None:
        from day4.today import Today
        self.generic_test(Today(), 513, 878)

    def test_day5(self) -> None:
        from day5.today import Today
        self.generic_test(Today(), "GRTSWNJHH", "QLFQDBBHM")

    def test_day6(self) -> None:
        from day6.today import Today
        self.generic_test(Today(), 1912, 2122)

    def test_day7(self) -> None:
        from day7.today import Today
        self.generic_test(Today(), 1517599, 2481982)

    def test_day8(self) -> None:
        from day8.today import Today
        self.generic_test(Today(), 1794, 199272)

    def test_day9(self) -> None:
        from day9.today import Today
        self.generic_test(Today(), 6197, 2562)

    def test_day10(self) -> None:
        from day10.today import Today
        ans2 = "####.####.###..####.#..#..##..#..#.###..\n" \
               "...#.#....#..#.#....#..#.#..#.#..#.#..#.\n" \
               "..#..###..###..###..####.#....#..#.#..#.\n" \
               ".#...#....#..#.#....#..#.#.##.#..#.###..\n" \
               "#....#....#..#.#....#..#.#..#.#..#.#....\n" \
               "####.#....###..#....#..#..###..##..#....\n."
        self.generic_test(Today(), 15680, ans2)

    def test_day11(self) -> None:
        from day11.today import Today
        self.generic_test(Today(), 120056, 21816744824)

    def test_day12(self) -> None:
        from day12.today import Today
        self.generic_test(Today(), 472, 465)


if __name__ == '__main__':
    unittest.main()
