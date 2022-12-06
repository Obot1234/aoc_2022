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


if __name__ == '__main__':
    unittest.main()
