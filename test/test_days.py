import unittest

from day import Day


class RegressionTestDays(unittest.TestCase):

    def generic_test(self, day: Day, first_answer: int, second_answer: int):
        self.assertEqual(day.part1(), first_answer, f"Problem with part 1 of day {day.day}")
        self.assertEqual(day.part2(), second_answer, f"Problem with part 2 of day {day.day}")

    def test_day1(self) -> None:
        from day1.day1 import Day1 as Today
        self.generic_test(Today(), 73211, 213958)

    def test_day2(self) -> None:
        from day2.day2 import Day2 as Today
        self.generic_test(Today(), 10404, 10334)

    def test_day3(self) -> None:
        from day3.day3 import Day3 as Today
        self.generic_test(Today(), 8088, 2522)


if __name__ == '__main__':
    unittest.main()
